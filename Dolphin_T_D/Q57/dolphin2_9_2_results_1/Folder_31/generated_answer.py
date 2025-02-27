import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_sum = np.sum(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for end_i in range(i + 1, matrix.shape[0] + 1):
                for end_j in range(j + 1, matrix.shape[1] + 1):
                    if np.sum(matrix[i:end_i, j:end_j]) == -44:
                        submatrices.append(matrix[i:end_i, j:end_j])
    if not submatrices:
        return []
    return submatrices