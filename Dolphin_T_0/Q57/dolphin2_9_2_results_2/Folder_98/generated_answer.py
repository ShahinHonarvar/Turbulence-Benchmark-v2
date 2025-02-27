import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    nrows = matrix.shape[0]
    ncols = matrix.shape[1]
    for i in range(nrows):
        for j in range(ncols):
            for i2 in range(i, nrows):
                for j2 in range(j, ncols):
                    if np.sum(matrix[i:i2 + 1, j:j2 + 1]) == 0:
                        submatrices.append(matrix[i:i2 + 1, j:j2 + 1])
    return submatrices