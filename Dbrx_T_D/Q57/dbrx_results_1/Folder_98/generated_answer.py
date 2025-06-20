import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrix = matrix[i:, j:]
            if np.sum(submatrix) == 0:
                submatrices.append(submatrix)
    return submatrices