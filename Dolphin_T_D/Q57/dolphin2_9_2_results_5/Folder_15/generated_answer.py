import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = np.array([])
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for width in range(1, min(matrix.shape[0] - i + 1, matrix.shape[1] - j + 1)):
                for height in range(1, min(matrix.shape[0] - i + 1, matrix.shape[1] - j + 1)):
                    submatrix_sum = np.sum(matrix[i:i + width, j:j + height])
                    if submatrix_sum == -9:
                        submatrices = np.concatenate((submatrices, [matrix[i:i + width, j:j + height]]))
    return submatrices