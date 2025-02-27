import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        submatrices = []
        rows, cols = mat.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        submatrices.append(mat[r1:r2 + 1, c1:c2 + 1])
        return submatrices
    submatrices = get_submatrices(matrix)
    result = []
    for submatrix in submatrices:
        if np.sum(submatrix) == -936:
            result.append(submatrix.tolist())
    return result