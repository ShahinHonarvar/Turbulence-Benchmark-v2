import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.shape == (n, n) and np.count_nonzero(submatrix == 37) == n * n:
                count += 1
    return count