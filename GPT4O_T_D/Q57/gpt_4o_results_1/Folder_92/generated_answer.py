import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape

    def find_submatrices(r1, c1, r2, c2):
        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
        if np.sum(submatrix) == -3:
            return submatrix.tolist()
        return None
    result = []
    for r1 in range(n):
        for r2 in range(r1, n):
            for c1 in range(m):
                for c2 in range(c1, m):
                    submatrix = find_submatrices(r1, c1, r2, c2)
                    if submatrix:
                        result.append(submatrix)
    return result