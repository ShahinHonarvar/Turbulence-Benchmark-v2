import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    result = []
    for i in range(0, row):
        for j in range(0, col):
            for k in range(i, row):
                for l in range(j, col):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 69:
                        result.append(matrix[i:k + 1, j:l + 1])
    return result