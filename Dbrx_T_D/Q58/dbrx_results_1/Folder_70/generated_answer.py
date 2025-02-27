import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 173 + 1):
        for j in range(n_cols - 173 + 1):
            submatrix = matrix[i:i + 173, j:j + 173]
            if np.sum(submatrix) == 173 * 173 * np.mean(submatrix):
                count += 1
    return count