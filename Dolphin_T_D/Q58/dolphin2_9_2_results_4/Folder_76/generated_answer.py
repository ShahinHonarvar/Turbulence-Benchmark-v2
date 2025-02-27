import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 159
    m, p = matrix.shape
    count = 0
    for i in range(m - n + 1):
        for j in range(p - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.sum(submatrix) == n * (n + 1) // 2:
                count += 1
    return count