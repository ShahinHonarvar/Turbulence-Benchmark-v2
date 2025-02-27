import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    submatrices_count = 0
    for row_start in range(n_rows):
        for col_start in range(n_cols):
            for row_end in range(row_start, n_rows):
                for col_end in range(col_start, n_cols):
                    submatrix_size = (row_end - row_start + 1) * (col_end - col_start + 1)
                    if submatrix_size == 85:
                        submatrices_count += 1
    return submatrices_count