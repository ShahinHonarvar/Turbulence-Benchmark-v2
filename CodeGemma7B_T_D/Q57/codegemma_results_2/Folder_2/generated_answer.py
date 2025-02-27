import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(i + 1, matrix.shape[0] + 1):
            for k in range(matrix.shape[1]):
                for l in range(k + 1, matrix.shape[1] + 1):
                    submatrix = matrix[i:j, k:l]
                    if np.sum(submatrix) == -863:
                        submatrices.append(submatrix)
    return submatrices