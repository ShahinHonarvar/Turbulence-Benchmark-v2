import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    counter = 0
    for i in range(m - 3):
        for j in range(n - 3):
            if np.sum(np.less_equal(matrix[i:i + 4, j:j + 4], 40)) == 40:
                counter += 1
    return counter