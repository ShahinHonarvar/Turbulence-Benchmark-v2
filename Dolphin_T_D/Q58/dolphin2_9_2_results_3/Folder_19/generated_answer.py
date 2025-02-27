import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 17
    rows, cols = matrix.shape
    count = 0
    for i in range(0, rows - n + 1):
        for j in range(0, cols - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                count += 1
    return count