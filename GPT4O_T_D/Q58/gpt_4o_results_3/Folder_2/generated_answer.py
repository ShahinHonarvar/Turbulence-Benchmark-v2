import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r_start in range(rows):
        for r_end in range(r_start, rows):
            for c_start in range(cols):
                for c_end in range(c_start, cols):
                    sub_row_count = r_end - r_start + 1
                    sub_col_count = c_end - c_start + 1
                    if sub_row_count * sub_col_count == 107:
                        count += 1
    return count