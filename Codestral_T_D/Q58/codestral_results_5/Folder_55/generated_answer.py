import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 39
    m, k = matrix.shape
    count = 0
    for i in range(m - n + 1):
        for j in range(k - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == 39 * 39:
                count += 1
    return count