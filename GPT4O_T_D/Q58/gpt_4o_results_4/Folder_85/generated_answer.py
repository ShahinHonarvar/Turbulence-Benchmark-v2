import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0]) if row_count > 0 else 0
    if row_count == 0 or col_count == 0 or row_count * col_count < 13:
        return 0
    count = 0
    possible_size = [3, 13]
    for rows in possible_size:
        for cols in possible_size:
            if rows * cols == 13 and rows <= row_count and (cols <= col_count):
                for i in range(row_count - rows + 1):
                    for j in range(col_count - cols + 1):
                        submatrix = matrix[i:i + rows, j:j + cols]
                        if submatrix.size == 13:
                            count += 1
    return count