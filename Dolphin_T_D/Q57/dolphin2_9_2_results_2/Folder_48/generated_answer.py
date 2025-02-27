import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for i2 in range(i, matrix.shape[0]):
                for j2 in range(j, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[i:i2 + 1, j:j2 + 1])
                    if submatrix_sum == -261:
                        submatrices.append(matrix[i:i2 + 1, j:j2 + 1])
    return submatrices