import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            for sub_rows in range(1, n_rows - i + 1):
                for sub_cols in range(1, n_cols - j + 1):
                    if sub_rows * sub_cols == 74:
                        count += 1
    return count