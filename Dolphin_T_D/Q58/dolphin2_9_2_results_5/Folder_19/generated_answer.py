import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            if matrix[i][j] != 0 and matrix[i + 1][j + 1] != 0 and (matrix[i + 2][j + 2] != 0) and (matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2] == 17):
                count += 1
    return count