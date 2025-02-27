import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 130
    rows, cols = matrix.shape
    counter = 0
    for r in range(rows - n + 1):
        for c in range(cols - n + 1):
            s = np.sum(matrix[r:r + n, c:c + n])
            if s == n * n * n:
                counter += 1
    return counter