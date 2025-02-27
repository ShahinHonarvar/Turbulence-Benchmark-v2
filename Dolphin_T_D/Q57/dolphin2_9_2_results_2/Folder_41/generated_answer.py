import numpy as np

def submatrix_with_particular_sum(matrix):
    row_length, col_length = matrix.shape
    submatrices = []
    for i in range(row_length):
        for j in range(col_length):
            for k in range(i, row_length):
                for l in range(j, col_length):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == -26:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices