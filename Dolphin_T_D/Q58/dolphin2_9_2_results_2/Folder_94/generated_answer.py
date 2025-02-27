import numpy as np

def submatrix_with_n_numbers(matrix):
    r, c = matrix.shape
    n = 93
    count = 0
    for i in range(r - n + 1):
        for j in range(c - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.count_nonzero(submatrix == n) == n * n:
                count += 1
    return count