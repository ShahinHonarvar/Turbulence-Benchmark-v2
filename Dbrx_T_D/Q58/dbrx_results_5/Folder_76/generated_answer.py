import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 159
    submatrices = []
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            submatrices.append(submatrix.flatten())
    return np.sum([np.count_nonzero(submatrix == n) for submatrix in submatrices])