import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows + 1):
        for j in range(cols + 1):
            for k in range(i, rows + 1):
                for l in range(j, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -65:
                        submatrices.append(submatrix)
    if submatrices:
        return submatrices
    else:
        return []