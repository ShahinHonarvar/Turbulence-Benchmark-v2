import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    num_rows, num_cols = matrix.shape
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            if matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] + matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 2][j + 1] + matrix[i][j + 2] + matrix[i + 1][j + 2] + matrix[i + 2][j + 2] == 173:
                count += 1
    return count