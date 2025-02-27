import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for r1 in range(n):
        for r2 in range(r1, n):
            for c1 in range(m):
                for c2 in range(c1, m):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(submatrix) == -36:
                        result.append(submatrix)
    return result