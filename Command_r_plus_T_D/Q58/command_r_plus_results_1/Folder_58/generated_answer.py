import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i][j] == 185 and matrix[i][j + 1] == 185 and (matrix[i + 1][j] == 185) and (matrix[i + 1][j + 1] == 185):
                count += 1
    return count