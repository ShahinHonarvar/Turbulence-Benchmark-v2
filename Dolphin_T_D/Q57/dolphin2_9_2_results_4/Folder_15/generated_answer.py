import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    h, w = matrix.shape
    for i, j in np.ndindex(h, w):
        for k, l in np.ndindex(h - i, w - j):
            if np.sum(matrix[i:i + k, j:j + l]) == -9:
                result.append(matrix[i:i + k, j:j + l])
    return result