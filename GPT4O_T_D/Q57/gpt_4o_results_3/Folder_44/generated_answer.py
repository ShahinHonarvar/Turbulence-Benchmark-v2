import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(i1, j1, i2, j2):
        submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
        return np.sum(submatrix)
    nrows, ncols = matrix.shape
    result = []
    for i1 in range(nrows):
        for i2 in range(i1, nrows):
            for j1 in range(ncols):
                for j2 in range(j1, ncols):
                    if get_submatrix_sum(i1, j1, i2, j2) == 830:
                        submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
                        result.append(submatrix.tolist())
    return result