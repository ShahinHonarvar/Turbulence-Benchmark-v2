import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    cnt = 0
    for i in range(m - 3):
        for j in range(n - 3):
            if np.sum(matrix[i:i + 4, j:j + 4]) == 85:
                cnt += 1
    return cnt