import numpy as np

def submatrix_with_particular_sum(matrix):
    shape = matrix.shape
    submatrices = []
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(i + 1, shape[0] + 1):
                for l in range(j + 1, shape[1] + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.sum() == -43:
                        submatrices.append(submatrix)
    return submatrices