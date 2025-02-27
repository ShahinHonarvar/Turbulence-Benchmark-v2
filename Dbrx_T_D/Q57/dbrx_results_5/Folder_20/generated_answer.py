import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows + 1):
        for j in range(cols + 1):
            for k in range(i + 1):
                for l in range(j + 1):
                    submatrix = matrix[k:i, l:j]
                    if np.sum(submatrix) == -57:
                        submatrices.append(submatrix)
    return submatrices