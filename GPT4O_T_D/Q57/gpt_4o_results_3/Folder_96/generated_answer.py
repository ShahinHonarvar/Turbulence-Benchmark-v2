import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(m, r1, r2, c1, c2):
        return m[r1:r2, c1:c2]

    def sum_of_matrix(m):
        return np.sum(m)
    rows, cols = matrix.shape
    result = []
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows + 1):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols + 1):
                    submatrix = get_submatrices(matrix, r1, r2, c1, c2)
                    if sum_of_matrix(submatrix) == -63:
                        result.append(submatrix)
    return result