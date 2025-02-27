import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    counter = 0
    for i in range(m - 2):
        for j in range(n - 2):
            if np.count_nonzero(matrix[i:i + 3, j:j + 3]) == 185:
                counter += 1
    return counter