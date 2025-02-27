import numpy as np

def submatrix_with_n_numbers(matrix):
    h, w = matrix.shape
    n = 33
    count = 0
    for i in range(h):
        for j in range(w):
            if matrix[i, j] == 0:
                if i + n <= h and j + n <= w:
                    if np.all(matrix[i:i + n, j:j + n] == 0):
                        count += 1
    return count