import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 3):
        for j in range(n - 3):
            if np.count_nonzero(matrix[i:i + 4, j:j + 4]) == 42:
                count += 1
    return count