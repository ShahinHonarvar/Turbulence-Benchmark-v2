import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    submatrix_count = 0
    for i in range(n_rows - 174):
        for j in range(n_cols - 174):
            submatrix = matrix[i:i + 175, j:j + 175]
            if submatrix.sum() == 175 * 175:
                submatrix_count += 1
    return submatrix_count