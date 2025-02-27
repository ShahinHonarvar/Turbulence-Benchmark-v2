import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size == 0:
        return 0
    m, n = matrix.shape
    cnt = 0
    for i in range(m - 2):
        for j in range(n - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 34:
                cnt += 1
    return cnt