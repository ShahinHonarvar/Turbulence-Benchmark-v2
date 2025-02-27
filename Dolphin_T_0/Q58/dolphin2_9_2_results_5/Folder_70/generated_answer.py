import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 173
    count = 0
    m, n = matrix.shape
    for i in range(m - n + 1):
        for j in range(n - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                count += 1
    return count