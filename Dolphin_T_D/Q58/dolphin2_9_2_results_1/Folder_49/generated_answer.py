import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 72
    rows, cols = matrix.shape
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.prod(matrix[i:i + n, j:j + n]) == n:
                count += 1
    return count