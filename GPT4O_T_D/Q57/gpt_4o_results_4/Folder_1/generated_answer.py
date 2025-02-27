import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        subs = []
        for r1 in range(rows):
            for r2 in range(r1 + 1, rows + 1):
                for c1 in range(cols):
                    for c2 in range(c1 + 1, cols + 1):
                        subs.append(mat[r1:r2, c1:c2])
        return subs
    submatrices = get_submatrices(matrix)
    result = []
    for sub in submatrices:
        if np.sum(sub) == -25:
            result.append(sub)
    return result