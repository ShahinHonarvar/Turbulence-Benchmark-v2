import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i1 in range(matrix.shape[0]):
        for i2 in range(i1, matrix.shape[0]):
            for j1 in range(matrix.shape[1]):
                for j2 in range(j1, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[i1:i2 + 1, j1:j2 + 1])
                    if submatrix_sum == 416:
                        submatrices.append(matrix[i1:i2 + 1, j1:j2 + 1].tolist())
    return submatrices