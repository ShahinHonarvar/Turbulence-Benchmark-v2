import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(0, matrix.shape[0] - 2):
        for j in range(0, matrix.shape[1] - 2):
            for k in range(i + 1, matrix.shape[0] - 1):
                for l in range(j + 1, matrix.shape[1] - 1):
                    if np.sum(matrix[i:k, j:l]) == -77:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices