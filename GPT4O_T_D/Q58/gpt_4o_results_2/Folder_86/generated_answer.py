import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for submatrix_rows in range(1, n_rows + 1):
        for submatrix_cols in range(1, n_cols + 1):
            submat_size = submatrix_rows * submatrix_cols
            if submat_size == 138:
                max_row_start = n_rows - submatrix_rows + 1
                max_col_start = n_cols - submatrix_cols + 1
                for row_start in range(max_row_start):
                    for col_start in range(max_col_start):
                        count += 1
    return count