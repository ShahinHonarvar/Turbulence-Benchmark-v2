import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    if rows * columns < 48:
        return 0
    count = 0
    for row_start in range(rows):
        for row_end in range(row_start + 1, rows + 1):
            for col_start in range(columns):
                for col_end in range(col_start + 1, columns + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.size == 48:
                        count += 1
    return count