import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    nrows, ncols = matrix.shape
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i, nrows):
                for l in range(j, ncols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -617:
                        submatrices.append(submatrix)
    return submatrices