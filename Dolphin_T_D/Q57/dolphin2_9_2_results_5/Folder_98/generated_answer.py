import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    h, w = matrix.shape
    for h0 in range(h + 1):
        for w0 in range(w + 1):
            for h1 in range(h0, h + 1):
                for w1 in range(w0, w + 1):
                    submatrix = matrix[h0:h1, w0:w1]
                    if np.sum(submatrix) == 0:
                        submatrices.append(submatrix)
    return submatrices