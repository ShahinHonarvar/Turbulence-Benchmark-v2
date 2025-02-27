import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i1 in range(matrix.shape[0]):
        for i2 in range(i1 + 1, matrix.shape[0]):
            for j1 in range(matrix.shape[1]):
                for j2 in range(j1 + 1, matrix.shape[1]):
                    submatrix = matrix[i1:i2, j1:j2]
                    if submatrix.sum() == -38:
                        submatrices.append(submatrix)
    return submatrices