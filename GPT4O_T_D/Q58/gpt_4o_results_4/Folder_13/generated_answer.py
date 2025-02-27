import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    total_elements = 175
    count = 0
    for top_row in range(row_count):
        for left_col in range(col_count):
            for bottom_row in range(top_row, row_count):
                for right_col in range(left_col, col_count):
                    if (bottom_row - top_row + 1) * (right_col - left_col + 1) == total_elements:
                        count += 1
    return count