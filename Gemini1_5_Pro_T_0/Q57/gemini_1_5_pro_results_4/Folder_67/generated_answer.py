import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrices = []
    for i1 in range(rows):
        for i2 in range(i1, rows):
            for j1 in range(cols):
                for j2 in range(j1, cols):
                    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
                    if np.sum(submatrix) == 40:
                        submatrices.append(submatrix)
    return submatrices