import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 84
    rows, cols = matrix.shape
    counter = 0
    for r in range(rows - n + 1):
        for c in range(cols - n + 1):
            if np.sum(matrix[r:r + n, c:c + n]) == n * n:
                counter += 1
    return counter