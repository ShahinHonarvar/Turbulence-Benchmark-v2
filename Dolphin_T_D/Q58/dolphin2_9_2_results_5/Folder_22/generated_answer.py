import numpy as np

def submatrix_with_n_numbers(matrix):
    h, w = matrix.shape
    count = 0
    for r in range(h - 2):
        for c in range(w - 2):
            if np.sum(matrix[r:r + 3, c:c + 3]) == 21:
                count += 1
    return count