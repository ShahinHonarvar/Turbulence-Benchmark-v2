import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        submat = mat[r1:r2 + 1, c1:c2 + 1]
                        if np.sum(submat) == -20:
                            yield submat
    return list(get_submatrices(matrix))