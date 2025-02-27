import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 93
    m, p = matrix.shape
    count = 0
    for i in range(m - n + 1):
        for j in range(p - n + 1):
            if np.count_nonzero(matrix[i:i + n, j:j + n]) == n:
                count += 1
    return count