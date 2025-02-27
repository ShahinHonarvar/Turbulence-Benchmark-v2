import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 64
    count = 0
    for i in range(rows - 7):
        for j in range(cols - 7):
            if np.prod(matrix[i:i + 8, j:j + 8].shape) == n:
                count += 1
    return count