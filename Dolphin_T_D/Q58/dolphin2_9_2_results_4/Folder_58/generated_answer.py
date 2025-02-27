import numpy as np

def submatrix_with_n_numbers(matrix):
    h, w = matrix.shape
    submatrix_count = 0
    for h1 in range(h - 2):
        for w1 in range(w - 2):
            if np.all(matrix[h1:h1 + 3, w1:w1 + 3] == 185):
                submatrix_count += 1
    return submatrix_count