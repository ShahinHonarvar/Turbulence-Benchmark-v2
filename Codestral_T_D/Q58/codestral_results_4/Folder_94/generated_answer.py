import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 93
    count = 0
    for r in range(rows - n + 1):
        for c in range(cols - n + 1):
            if np.count_nonzero(matrix[r:r + n, c:c + n] == 93) == n:
                count += 1
    return count