import numpy as np

def submatrix_with_n_numbers(matrix):
    row_num, col_num = matrix.shape
    submatrix_count = 0
    for upper_row in range(row_num):
        for upper_col in range(col_num):
            for lower_row in range(upper_row, row_num):
                for lower_col in range(upper_col, col_num):
                    if (lower_row - upper_row + 1) * (lower_col - upper_col + 1) == 127:
                        submatrix_count += 1
    return submatrix_count