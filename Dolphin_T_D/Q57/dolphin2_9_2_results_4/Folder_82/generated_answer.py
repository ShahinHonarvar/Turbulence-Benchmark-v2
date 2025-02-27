import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    h, w = matrix.shape
    for r1 in range(h):
        for c1 in range(w):
            for r2 in range(r1, h):
                for c2 in range(c1, w):
                    if np.sum(matrix[r1:r2 + 1, c1:c2 + 1]) == -27:
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return result