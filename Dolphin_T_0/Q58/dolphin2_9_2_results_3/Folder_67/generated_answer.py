import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 3):
        for j in range(n_cols - 3):
            if np.sum(matrix[i:i + 4, j:j + 4]) == 43:
                count += 1
    return count