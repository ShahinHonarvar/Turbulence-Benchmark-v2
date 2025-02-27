import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 41
    height, width = matrix.shape
    count = 0
    for i in range(height - n + 1):
        for j in range(width - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                count += 1
    return count