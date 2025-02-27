import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(columns):
            for s in range(i + 1, rows + 1):
                for t in range(j + 1, columns + 1):
                    if np.sum(matrix[i:s, j:t]) == 41:
                        submatrices.append(matrix[i:s, j:t])
    return submatrices