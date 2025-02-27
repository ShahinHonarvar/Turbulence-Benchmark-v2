import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            for x in range(i, row):
                for y in range(j, col):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == 997:
                        submatrices.append(matrix[i:x + 1, j:y + 1])
    return submatrices