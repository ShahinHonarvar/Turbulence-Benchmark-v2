import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    h, w = matrix.shape
    for i in range(h):
        for j in range(i, h):
            for k in range(w):
                for l in range(k, w):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if np.sum(submatrix) == 1:
                        submatrices.append(submatrix)
    return submatrices