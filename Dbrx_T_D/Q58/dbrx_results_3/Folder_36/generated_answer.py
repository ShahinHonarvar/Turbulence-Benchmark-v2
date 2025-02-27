import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_numbers(submatrix):
        return np.sum(np.where(submatrix == 13, 1, 0))
    nrows, ncols = matrix.shape
    result = 0
    for i in range(nrows - 1):
        for j in range(ncols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            result += count_numbers(submatrix)
    return result