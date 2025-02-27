import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (i + 2 < rows and j + 2 < cols) and matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] + matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 2][j + 1] + matrix[i][j + 2] + matrix[i + 1][j + 2] + matrix[i + 2][j + 2] == 7:
                count += 1
    return count