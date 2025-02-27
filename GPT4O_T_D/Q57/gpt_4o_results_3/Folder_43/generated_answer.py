import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        yield matrix[r1:r2 + 1, c1:c2 + 1]

    def submatrix_sum(submat):
        return np.sum(submat)
    result = []
    for submat in get_submatrices(matrix):
        if submatrix_sum(submat) == -81:
            result.append(submat)
    return result