import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    curr_sum = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
                    if curr_sum == -90:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return submatrices