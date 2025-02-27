import numpy as np

def submatrix_with_particular_sum(mat):
    row, col = mat.shape
    submatrices = []
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    submatrix = mat[i:k + 1, j:l + 1]
                    if submatrix.sum() == -37:
                        submatrices.append(submatrix)
    return submatrices