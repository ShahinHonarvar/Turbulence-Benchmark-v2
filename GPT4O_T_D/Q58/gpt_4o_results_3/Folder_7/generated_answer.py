import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    submatrix_count = 0
    for row_start in range(n_rows):
        for col_start in range(n_cols):
            for row_end in range(row_start + 1, n_rows + 1):
                for col_end in range(col_start + 1, n_cols + 1):
                    if (row_end - row_start) * (col_end - col_start) == 121:
                        submatrix_count += 1
    return submatrix_count