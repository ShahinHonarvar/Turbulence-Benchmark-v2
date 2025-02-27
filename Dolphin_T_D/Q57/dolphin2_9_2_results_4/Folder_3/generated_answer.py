import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    submatrices = []
    for i in range(row):
        for j in range(col):
            for i_end in range(i + 1, row + 1):
                for j_end in range(j + 1, col + 1):
                    submatrix = matrix[i:i_end, j:j_end]
                    if np.sum(submatrix) == 54:
                        submatrices.append(submatrix)
    return submatrices