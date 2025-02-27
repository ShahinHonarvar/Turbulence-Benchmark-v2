import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    total_sum = np.sum(matrix)
    submatrices = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    sub_sum = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
                    if sub_sum == -47 and (r1 != r2 or c1 != c2):
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return submatrices