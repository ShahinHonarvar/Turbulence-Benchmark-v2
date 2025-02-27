import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 97
    count = 0

    def has_n_integers(submatrix):
        return np.count_nonzero(submatrix == n) == n
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for row in range(i, matrix.shape[0]):
                for col in range(j, matrix.shape[1]):
                    submatrix = matrix[i:row + 1, j:col + 1]
                    if has_n_integers(submatrix):
                        count += 1
    return count