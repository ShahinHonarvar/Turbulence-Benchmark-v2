import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for n in range(i, matrix.shape[0]):
                for m in range(j, matrix.shape[1]):
                    if np.sum(matrix[i:n + 1, j:m + 1]) == 93:
                        submatrices.append(matrix[i:n + 1, j:m + 1])
    return submatrices