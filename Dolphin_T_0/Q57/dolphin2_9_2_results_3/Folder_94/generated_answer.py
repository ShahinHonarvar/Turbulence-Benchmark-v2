import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 92:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices