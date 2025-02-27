import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        yield matrix[r1:r2 + 1, c1:c2 + 1]
    submatrices = list(get_submatrices(matrix))
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == -25]
    return result