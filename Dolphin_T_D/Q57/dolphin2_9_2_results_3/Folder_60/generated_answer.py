import numpy as np

def submatrix_with_particular_sum(matrix):
    h, w = matrix.shape
    submatrices = []
    for i in range(h):
        for j in range(w):
            for h_s in range(i, h):
                for w_s in range(j, w):
                    if np.sum(matrix[i:h_s + 1, j:w_s + 1]) == 94:
                        submatrices.append(matrix[i:h_s + 1, j:w_s + 1])
    return submatrices