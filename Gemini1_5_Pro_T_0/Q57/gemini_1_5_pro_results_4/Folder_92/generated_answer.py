import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for m in range(i + 1, rows + 1):
                for n in range(j + 1, cols + 1):
                    submatrix = matrix[i:m, j:n]
                    if np.sum(submatrix) == -3:
                        submatrices.append(submatrix)
    return submatrices