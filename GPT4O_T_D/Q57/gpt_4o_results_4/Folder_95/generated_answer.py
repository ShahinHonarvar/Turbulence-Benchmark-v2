import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        yield mat[r1:r2 + 1, c1:c2 + 1]
    result = []
    for submatrix in get_submatrices(matrix):
        if np.sum(submatrix) == 19:
            result.append(submatrix)
    return result