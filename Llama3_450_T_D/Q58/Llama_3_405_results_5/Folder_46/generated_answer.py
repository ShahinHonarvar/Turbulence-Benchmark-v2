import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_size = 144
    count = 0
    for row in range(rows):
        for col in range(cols):
            for sub_row_size in range(1, rows - row + 1):
                for sub_col_size in range(1, cols - col + 1):
                    if sub_row_size * sub_col_size == target_size:
                        submatrix = matrix[row:row + sub_row_size, col:col + sub_col_size]
                        if submatrix.size == target_size:
                            count += 1
    return count