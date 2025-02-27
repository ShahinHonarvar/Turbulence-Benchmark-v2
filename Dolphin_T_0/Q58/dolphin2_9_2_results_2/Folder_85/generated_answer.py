import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 13
    h, w = matrix.shape
    count = 0
    for i in range(h - n + 1):
        for j in range(w - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                count += 1
    return count