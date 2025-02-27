import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 8
    m = matrix.shape[0]
    l = matrix.shape[1]
    count = 0
    for i in range(m - n + 1):
        for j in range(l - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == 68 * n:
                count += 1
    return count