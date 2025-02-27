import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    submatrices = []
    for i in range(row):
        for j in range(col):
            for k in range(i + 1, row + 1):
                for l in range(j + 1, col + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 64:
                        submatrices.append(submatrix)
    return submatrices