import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(rows):
        for c in range(cols):
            for r2 in range(r, rows):
                for c2 in range(c, cols):
                    submatrix = matrix[r:r2 + 1, c:c2 + 1]
                    if np.sum(submatrix) == 88:
                        submatrices.append(submatrix)
    return submatrices