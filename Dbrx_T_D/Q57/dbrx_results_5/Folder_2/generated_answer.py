import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for p in range(i, matrix.shape[0]):
                for q in range(j, matrix.shape[1]):
                    submatrix = matrix[i:p + 1, j:q + 1]
                    if np.sum(submatrix) == -863:
                        submatrices.append(submatrix)
    return submatrices