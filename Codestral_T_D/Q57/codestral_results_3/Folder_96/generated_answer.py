import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0] + 1):
                for l in range(j, matrix.shape[1] + 1):
                    if np.sum(matrix[i:k, j:l]) == -63:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices