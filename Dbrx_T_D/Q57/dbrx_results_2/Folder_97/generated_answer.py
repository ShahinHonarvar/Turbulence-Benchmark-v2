import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for height in range(row + 1, matrix.shape[0] - 1):
                for width in range(col + 1, matrix.shape[1] - 1):
                    submatrix = matrix[row:height, col:width]
                    if np.sum(submatrix) == -617:
                        submatrices.append(submatrix)
    return submatrices