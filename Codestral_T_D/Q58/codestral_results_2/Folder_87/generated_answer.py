import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 96
    count = 0
    for i in range(rows - n // 8 + 1):
        for j in range(cols - n // 8 + 1):
            if np.sum(matrix[i:i + n // 8, j:j + n // 8]) == n:
                count += 1
    return count