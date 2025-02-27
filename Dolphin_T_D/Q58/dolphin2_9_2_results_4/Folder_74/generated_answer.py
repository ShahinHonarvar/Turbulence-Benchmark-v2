import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    counter = 0
    for i in range(m - 5):
        for j in range(n - 5):
            if np.count_nonzero(matrix[i:i + 6, j:j + 6]) == 48:
                counter = counter + 1
    return counter