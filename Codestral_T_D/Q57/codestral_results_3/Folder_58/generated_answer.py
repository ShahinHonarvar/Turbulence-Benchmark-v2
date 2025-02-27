import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(rows):
        for c in range(cols):
            for r_end in range(r, rows):
                for c_end in range(c, cols):
                    submatrix = matrix[r:r_end + 1, c:c_end + 1]
                    if np.sum(submatrix) == -137:
                        submatrices.append(submatrix)
    return submatrices