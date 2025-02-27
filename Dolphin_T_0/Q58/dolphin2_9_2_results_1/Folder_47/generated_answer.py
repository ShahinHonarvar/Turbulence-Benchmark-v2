import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 90
    s = matrix.shape
    c = 0
    for i in range(s[0] - n + 1):
        for j in range(s[1] - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                c += 1
    return c