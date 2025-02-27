import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 64
    shape = matrix.shape
    count = 0
    for r in range(shape[0] - n + 1):
        for c in range(shape[1] - n + 1):
            submatrix = matrix[r:r + n, c:c + n]
            count += np.prod(submatrix == n)
    return count