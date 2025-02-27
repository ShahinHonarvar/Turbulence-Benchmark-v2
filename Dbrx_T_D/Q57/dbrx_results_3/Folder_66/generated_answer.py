import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for height in range(1, matrix.shape[0] - row + 1):
                for width in range(1, matrix.shape[1] - col + 1):
                    submatrix = matrix[row:row + height, col:col + width]
                    if np.sum(submatrix) == 99:
                        submatrices.append(submatrix)
    return submatrices