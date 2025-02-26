import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for r1 in range(m):
        for r2 in range(r1, m):
            for c1 in range(n):
                for c2 in range(c1, n):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(submatrix) == 382:
                        result.append(submatrix.tolist())
    return result