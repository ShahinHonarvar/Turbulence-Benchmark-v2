import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix[i].shape[0]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix[i].shape[0]):
                    sub = np.sum(matrix[i:k + 1, j:l + 1])
                    if sub == -157 and (i != k or j != l):
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices