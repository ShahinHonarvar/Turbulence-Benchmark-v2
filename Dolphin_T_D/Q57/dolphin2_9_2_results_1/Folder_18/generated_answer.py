import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return []
    submatrices = []
    for ii in range(matrix.shape[0]):
        for jj in range(matrix.shape[1]):
            for kk in range(ii + 1, matrix.shape[0] + 1):
                for ll in range(jj + 1, matrix.shape[1] + 1):
                    if np.sum(matrix[ii:kk, jj:ll]) == 616:
                        submatrices.append(matrix[ii:kk, jj:ll])
    return submatrices