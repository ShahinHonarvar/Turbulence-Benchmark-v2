import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for sub_rows in range(1, n_rows + 1):
        for sub_cols in range(1, n_cols + 1):
            if sub_rows * sub_cols == 48:
                for i in range(n_rows - sub_rows + 1):
                    for j in range(n_cols - sub_cols + 1):
                        count += 1
    return count