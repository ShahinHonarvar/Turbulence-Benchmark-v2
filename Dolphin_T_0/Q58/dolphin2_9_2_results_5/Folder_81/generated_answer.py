import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 97
    matrix = np.array(matrix)
    h, w = matrix.shape
    cnt = 0
    for i in range(h - n + 1):
        for j in range(w - n + 1):
            if np.sum(matrix[i:i + n, j:j + n] == 0) == 0:
                cnt += 1
    return cnt