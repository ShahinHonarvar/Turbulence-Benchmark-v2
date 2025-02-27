import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 1):
        for j in range(n - 1):
            if np.sum(matrix[i:i + 2, j:j + 2]) == 46:
                count += 1
    return count