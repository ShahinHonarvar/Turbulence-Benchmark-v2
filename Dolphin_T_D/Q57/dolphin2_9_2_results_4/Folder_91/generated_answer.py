import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    result = []
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == -6:
                        result.append(matrix[i:k + 1, j:l + 1])
    return result