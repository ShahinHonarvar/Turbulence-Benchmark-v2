import numpy as np

def submatrix_with_particular_sum(matrix):

    def calculate_submatrix_sum(mat, i1, j1, i2, j2):
        return np.sum(mat[i1:i2 + 1, j1:j2 + 1])
    rows, cols = matrix.shape
    submatrices = []
    for i1 in range(rows):
        for j1 in range(cols):
            for i2 in range(i1, rows):
                for j2 in range(j1, cols):
                    if calculate_submatrix_sum(matrix, i1, j1, i2, j2) == -57:
                        submatrix = matrix[i1:i2 + 1, j1:j2 + 1].tolist()
                        submatrices.append(submatrix)
    return submatrices