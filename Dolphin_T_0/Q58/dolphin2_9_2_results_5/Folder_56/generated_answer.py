import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 5 + 1):
        for j in range(n - 8 + 1):
            if np.count_nonzero(matrix[i:i + 6, j:j + 8]) == 64:
                count += 1
    return count