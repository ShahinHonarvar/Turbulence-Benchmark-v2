import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(rows):
        for c in range(cols):
            for r_end in range(r + 1, rows + 1):
                for c_end in range(c + 1, cols + 1):
                    submatrix = matrix[r:r_end, c:c_end]
                    if np.sum(submatrix) == -452:
                        submatrices.append(submatrix)
    return submatrices