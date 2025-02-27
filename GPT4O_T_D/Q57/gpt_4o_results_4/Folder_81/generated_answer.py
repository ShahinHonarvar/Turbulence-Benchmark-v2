import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(r1, r2, c1, c2):
        return np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
    n, m = matrix.shape
    result = []
    for r1 in range(n):
        for r2 in range(r1, n):
            for c1 in range(m):
                for c2 in range(c1, m):
                    if submatrix_sum(r1, r2, c1, c2) == -90:
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1].copy())
    return result