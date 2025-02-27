import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 7):
        for j in range(n - 7):
            if np.sum(matrix[i:i + 8, j:j + 8]) == 96:
                count += 1
    return count