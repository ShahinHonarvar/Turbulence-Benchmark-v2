import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(mat, r1, c1, r2, c2):
        return np.sum(mat[r1:r2 + 1, c1:c2 + 1])
    rows, cols = matrix.shape
    result = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    if get_submatrix_sum(matrix, r1, c1, r2, c2) == -37:
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1].tolist())
    return result