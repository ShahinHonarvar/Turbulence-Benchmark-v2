import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for height in range(1, matrix.shape[0] - i + 1):
                for width in range(1, matrix.shape[1] - j + 1):
                    submatrix = matrix[i:i + height, j:j + width]
                    if np.sum(submatrix) == 41:
                        submatrices.append(submatrix)
    return submatrices