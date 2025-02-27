import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_matrix(submatrix):
        return np.sum(submatrix)
    nrows, ncols = matrix.shape
    submatrices = []
    for r1 in range(nrows):
        for r2 in range(r1, nrows):
            for c1 in range(ncols):
                for c2 in range(c1, ncols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if sum_matrix(submatrix) == 93:
                        submatrices.append(submatrix)
    return submatrices