import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    result = []
    for i in range(row - 2):
        for j in range(col - 2):
            s = matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 2][j] + matrix[i][j + 2] + matrix[i + 1][j + 2] + matrix[i + 2][j + 1]
            if s == 88:
                tmp = matrix[i:i + 3, j:j + 3]
                result.append(tmp)
    return result