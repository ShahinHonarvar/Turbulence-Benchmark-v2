import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 57
    submatrices_count = 0
    for sub_row_start in range(rows):
        for sub_col_start in range(cols):
            for sub_row_end in range(sub_row_start, rows):
                for sub_col_end in range(sub_col_start, cols):
                    if (sub_row_end - sub_row_start + 1) * (sub_col_end - sub_col_start + 1) == target_count:
                        submatrices_count += 1
    return submatrices_count