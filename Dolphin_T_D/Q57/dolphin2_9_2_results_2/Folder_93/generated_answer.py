import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    nrow, ncol = matrix.shape
    for i1 in range(nrow):
        for i2 in range(i1, nrow):
            for j1 in range(ncol):
                for j2 in range(j1, ncol):
                    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
                    if np.sum(submatrix) == -65:
                        submatrices.append(submatrix)
    return submatrices