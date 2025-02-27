import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 90
    m, p = matrix.shape
    counter = 0
    for i in range(m - n + 1):
        for j in range(p - n + 1):
            if np.array_equal(matrix[i:i + n, j:j + n].reshape(n), np.arange(1, n + 1)):
                counter += 1
    return counter