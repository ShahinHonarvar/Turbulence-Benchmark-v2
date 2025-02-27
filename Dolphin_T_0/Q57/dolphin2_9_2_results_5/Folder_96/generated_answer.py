import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == -63:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices