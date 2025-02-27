import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    h, w = matrix.shape
    for i in range(h):
        for j in range(w):
            for k in range(i, h):
                for l in range(j, w):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 56:
                        result.append(matrix[i:k + 1, j:l + 1])
    return result