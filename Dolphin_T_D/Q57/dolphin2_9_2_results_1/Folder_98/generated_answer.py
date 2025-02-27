import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return []
    submatrices = []
    rows, cols = matrix.shape
    for i1 in range(rows):
        for j1 in range(cols):
            for i2 in range(i1, rows):
                for j2 in range(j1, cols):
                    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
                    if np.sum(submatrix) == 0:
                        submatrices.append(submatrix)
    return submatrices