import numpy as np

def submatrix_with_n_numbers(matrix):
    total = 0
    n = 173
    h, w = matrix.shape
    for i in range(h - n + 1):
        for j in range(w - n + 1):
            if np.count_nonzero(matrix[i:i + n, j:j + n]) == n:
                total += 1
    return total