import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 21
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.prod(matrix[i:i + n, j:j + n].shape) == 21:
                count += 1
    return count