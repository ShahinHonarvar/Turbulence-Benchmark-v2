import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix(i, j, k, l):
        return matrix[i:k, j:l]

    def get_matrix_sum(matrix):
        return np.sum(matrix)
    n, m = matrix.shape
    submatrices = []
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n):
                for l in range(j + 1, m):
                    submatrix = get_submatrix(i, j, k, l)
                    if get_matrix_sum(submatrix) == -137:
                        submatrices.append(submatrix)
    return submatrices