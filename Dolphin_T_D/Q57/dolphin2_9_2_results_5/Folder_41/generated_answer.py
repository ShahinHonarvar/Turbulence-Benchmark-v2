import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for i in range(nrows):
        for j in range(ncols):
            for iend in range(i, nrows):
                for jend in range(j, ncols):
                    submatrix_sum = np.sum(matrix[i:iend + 1, j:jend + 1])
                    if submatrix_sum == -26:
                        submatrices.append(matrix[i:iend + 1, j:jend + 1])
    return submatrices