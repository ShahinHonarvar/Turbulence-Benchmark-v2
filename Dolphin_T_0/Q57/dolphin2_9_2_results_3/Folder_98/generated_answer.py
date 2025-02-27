import numpy as np

def submatrix_with_particular_sum(matrix):
    h, w = matrix.shape
    submatrices = []
    for i in range(h):
        for j in range(w):
            for h2 in range(i, h):
                for w2 in range(j, w):
                    sub = matrix[i:h2 + 1, j:w2 + 1]
                    if np.sum(sub) == 0:
                        submatrices.append(sub)
    return submatrices