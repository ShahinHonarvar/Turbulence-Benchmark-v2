import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for i2 in range(i, rows):
                for j2 in range(j, cols):
                    if np.sum(matrix[i:i2 + 1, j:j2 + 1]) == 13:
                        submatrices.append(matrix[i:i2 + 1, j:j2 + 1])
    return submatrices