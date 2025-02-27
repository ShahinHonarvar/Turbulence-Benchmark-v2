import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    sub = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub) == -36:
                        submatrices.append(sub)
    return submatrices