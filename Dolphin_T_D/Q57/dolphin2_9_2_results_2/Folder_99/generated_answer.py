import numpy as np

def submatrix_with_particular_sum(matrix):
    R, C = matrix.shape
    submatrices = []
    for r1 in range(R):
        for c1 in range(C):
            for r2 in range(r1 + 1, R + 1):
                for c2 in range(c1 + 1, C + 1):
                    if np.sum(matrix[r1:r2, c1:c2]) == -185:
                        submatrices.append(matrix[r1:r2, c1:c2])
    return submatrices