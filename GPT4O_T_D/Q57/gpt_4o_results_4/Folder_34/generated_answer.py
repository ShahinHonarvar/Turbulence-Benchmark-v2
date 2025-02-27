import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_of_submatrix(mat, r1, c1, r2, c2):
        sub_sum = 0
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                sub_sum += mat[i, j]
        return sub_sum
    rows, cols = matrix.shape
    submatrices = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    if sum_of_submatrix(matrix, r1, c1, r2, c2) == -13:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1].tolist())
    return submatrices