import numpy as np

def submatrix_with_n_numbers(matrix):
    n_numbers = 77
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            if np.sum(matrix[i:i + i, j:j + i]) == n_numbers:
                count += 1
    return count