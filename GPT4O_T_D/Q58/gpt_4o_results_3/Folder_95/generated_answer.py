import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    rows_num = end_row - start_row + 1
                    cols_num = end_col - start_col + 1
                    if rows_num * cols_num == 87:
                        submatrix_count += 1
    return submatrix_count