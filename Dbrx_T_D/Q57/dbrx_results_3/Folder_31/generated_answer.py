import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0] - 1):
        for j in range(matrix_shape[1] - 1):
            for k in range(i, matrix_shape[0]):
                for l in range(j, matrix_shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -44:
                        submatrices.append(submatrix)
    return submatrices