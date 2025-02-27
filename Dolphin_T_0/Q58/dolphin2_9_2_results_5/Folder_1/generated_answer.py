import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 23
    h, w = matrix.shape
    for i in range(h - n + 1):
        for j in range(w - n + 1):
            if np.all(matrix[i:i + n, j:j + n] >= 0) and np.all(matrix[i:i + n, j:j + n] <= 9):
                count += 1
    return count