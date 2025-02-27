import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n - 39 + 1):
        for j in range(m - 39 + 1):
            submatrix = matrix[i:i + 39, j:j + 39]
            if np.count_nonzero(submatrix == 39) == 39 * 39:
                count += 1
    return count