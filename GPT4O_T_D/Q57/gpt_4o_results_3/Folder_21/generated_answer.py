import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(i1, j1, i2, j2):
        return np.sum(matrix[i1:i2 + 1, j1:j2 + 1])
    submatrices = []
    rows, cols = matrix.shape
    for i1 in range(rows):
        for j1 in range(cols):
            for i2 in range(i1, rows):
                for j2 in range(j1, cols):
                    if get_submatrix_sum(i1, j1, i2, j2) == -936:
                        submatrices.append(matrix[i1:i2 + 1, j1:j2 + 1])
    return submatrices