import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for r2 in range(r, rows):
                for c2 in range(c, cols):
                    if np.sum(matrix[r:r2, c:c2]) == 99 and [r, r2, c, c2] not in submatrices:
                        submatrices.append([r, r2, c, c2])
    return submatrices