import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    counter = 0
    for r in range(0, m - 7):
        for c in range(0, n - 8):
            submatrix = matrix[r:r + 8, c:c + 8]
            if np.count_nonzero(submatrix) == 64:
                counter += 1
    return counter