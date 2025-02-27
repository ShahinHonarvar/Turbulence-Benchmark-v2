import numpy as np

def submatrix_with_particular_sum(matrix):
    h, w = matrix.shape
    result = []
    for i in range(h):
        for j in range(w):
            for k in range(i + 1, h + 1):
                for l in range(j + 1, w + 1):
                    if np.sum(matrix[i:k, j:l]) == 382:
                        result.append(matrix[i:k, j:l])
    return result