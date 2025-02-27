import numpy as np

def submatrix_with_particular_sum(matrix):
    if matrix.shape[0] < matrix.shape[1]:
        matrix = np.rot90(matrix)
    if matrix[0][0] != 0:
        matrix[0][0] = 0
    submatrices = [matrix[0].tolist()]
    for i in range(1, matrix.shape[0]):
        for j in range(1, matrix.shape[1]):
            if matrix[i][j] == 66:
                submatrices.append(matrix[i].tolist())
                submatrices += submatrix_with_particular_sum(matrix[i])
    return submatrices