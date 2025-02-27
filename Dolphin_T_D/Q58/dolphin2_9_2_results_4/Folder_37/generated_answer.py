import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    cnt = 0
    for i in range(m - 7):
        for j in range(n - 7):
            if np.prod(matrix[i:i + 8, j:j + 8] == 64) != 0:
                cnt += 1
    return cnt