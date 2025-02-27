import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    if np.sum(matrix[i:k, j:l]) == 92:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices