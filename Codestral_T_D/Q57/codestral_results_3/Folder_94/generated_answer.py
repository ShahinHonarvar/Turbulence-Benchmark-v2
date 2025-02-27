import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for rr in range(r, rows):
                for cc in range(c, cols):
                    submatrix = matrix[r:rr + 1, c:cc + 1]
                    if np.sum(submatrix) == 92:
                        submatrices.append(submatrix.tolist())
    return submatrices