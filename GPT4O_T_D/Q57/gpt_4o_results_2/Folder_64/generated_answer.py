import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(r1, c1, r2, c2):
        return np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
    m, n = matrix.shape
    result = []
    for r1 in range(m):
        for r2 in range(r1, m):
            for c1 in range(n):
                for c2 in range(c1, n):
                    if submatrix_sum(r1, c1, r2, c2) == -4:
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1].tolist())
    return result