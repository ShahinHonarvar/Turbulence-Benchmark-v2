import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, columns + 1):
                    if np.sum(matrix[i:k, j:l]) == -4 and [i, j, k, l] not in submatrices:
                        submatrices.append([i, j, k, l])
    return submatrices