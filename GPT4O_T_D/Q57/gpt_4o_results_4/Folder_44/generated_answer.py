import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, top, left, bottom, right):
        return np.sum(mat[top:bottom + 1, left:right + 1])
    nrows, ncols = matrix.shape
    result = []
    for top in range(nrows):
        for left in range(ncols):
            for bottom in range(top, nrows):
                for right in range(left, ncols):
                    if submatrix_sum(matrix, top, left, bottom, right) == 830:
                        result.append(matrix[top:bottom + 1, left:right + 1].tolist())
    return result