import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    submatrices = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submatrix = mat[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(submatrix) == -394:
                        submatrices.append(submatrix)
    return submatrices