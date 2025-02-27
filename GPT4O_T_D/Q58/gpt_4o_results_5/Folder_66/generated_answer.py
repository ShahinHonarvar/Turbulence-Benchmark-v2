import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    submatrix_size = 42
    for row_size in range(1, n_rows + 1):
        for col_size in range(1, n_cols + 1):
            if row_size * col_size == submatrix_size:
                for i in range(n_rows - row_size + 1):
                    for j in range(n_cols - col_size + 1):
                        count += 1
    return count