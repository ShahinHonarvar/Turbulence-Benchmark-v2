import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    m = matrix.shape[1]
    for i in range(n):
        for j in range(m):
            if i + 2 < n and j + 2 < m:
                if np.all(matrix[i:i + 2, j:j + 2] == 5):
                    return np.sum(np.ones((n, m)))
    return 0