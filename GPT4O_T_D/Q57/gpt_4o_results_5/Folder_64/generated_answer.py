import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for r1 in range(nrows):
        for r2 in range(r1, nrows):
            for c1 in range(ncols):
                for c2 in range(c1, ncols):
                    submatrix_sum = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
                    if submatrix_sum == -4:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1].tolist())
    return submatrices