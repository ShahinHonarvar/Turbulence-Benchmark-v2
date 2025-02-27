import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols):
                    subarray = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(subarray) == 99:
                        submatrices.append(subarray)
    return submatrices