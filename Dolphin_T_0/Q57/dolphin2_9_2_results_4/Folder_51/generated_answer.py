import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    row_length, col_length = matrix.shape
    for i in range(row_length):
        for j in range(col_length):
            for k in range(i + 1, row_length + 1):
                for l in range(j + 1, col_length + 1):
                    if np.sum(matrix[i:k, j:l]) == -46:
                        result.append(matrix[i:k, j:l].tolist())
    return result