import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    sub = matrix[i:r + 1, j:c + 1]
                    if np.sum(sub) == 245:
                        submatrices.append(sub)
    return submatrices if submatrices else []