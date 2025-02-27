import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(i + 1, rows + 1):
            for k in range(cols):
                for l in range(k + 1, cols + 1):
                    submatrix = matrix[i:j, k:l]
                    if np.sum(submatrix) == 56:
                        submatrices.append(submatrix.tolist())
    return submatrices