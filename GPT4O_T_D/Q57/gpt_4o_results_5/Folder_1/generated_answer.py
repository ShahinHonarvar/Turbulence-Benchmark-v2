import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat):
        return np.sum(mat)
    submatrices = []
    rows, cols = matrix.shape
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submat = matrix[r1:r2 + 1, c1:c2 + 1]
                    if sum_submatrix(submat) == -25:
                        submatrices.append(submat.copy())
    return submatrices