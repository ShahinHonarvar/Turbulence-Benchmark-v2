import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    result = 0
    for i in range(n_rows - 2):
        for j in range(n_cols - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 60:
                result += 1
    return result