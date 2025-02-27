import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    result = []
    for i in range(row):
        for j in range(col):
            for k in range(i + 1, row + 1):
                for l in range(j + 1, col + 1):
                    if np.sum(matrix[i:k, j:l]) == -43:
                        result.append(matrix[i:k, j:l])
    return result