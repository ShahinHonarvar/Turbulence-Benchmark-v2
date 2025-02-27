import numpy as np

def submatrix_with_particular_sum(matrix):
    num_rows, num_cols = matrix.shape
    submatrices = []
    for r1 in range(num_rows):
        for r2 in range(r1, num_rows):
            for c1 in range(num_cols):
                for c2 in range(c1, num_cols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(submatrix) == -57:
                        submatrices.append(submatrix.tolist())
    return submatrices