import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for size_x in range(1, matrix.shape[0] - i + 1):
                for size_y in range(1, matrix.shape[1] - j + 1):
                    submatrix = matrix[i:i + size_x, j:j + size_y]
                    if np.sum(submatrix) == 1:
                        submatrices.append(submatrix)
    return submatrices