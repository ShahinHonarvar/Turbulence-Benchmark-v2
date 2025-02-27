import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        return []
    h, w = matrix.shape
    result = []
    for i in range(h):
        for j in range(w):
            for k in range(i, h):
                for l in range(j, w):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -27:
                        result.append(submatrix.tolist())
    return result