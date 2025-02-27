import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    result = []
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub_matrix) == -15:
                        result.append(sub_matrix)
    return result