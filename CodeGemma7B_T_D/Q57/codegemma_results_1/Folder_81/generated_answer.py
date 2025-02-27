import numpy as np

def submatrix_with_particular_sum(matrix):
    matrix = matrix.cumsum(axis=0).cumsum(axis=1)
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix_sum = matrix[k, l] - matrix[i, l] - matrix[k, j] + matrix[i, j]
                    if submatrix_sum == -90:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices if submatrices else []