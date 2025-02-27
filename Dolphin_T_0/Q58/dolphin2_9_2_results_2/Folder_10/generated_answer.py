import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 56:
                if i > 0 and j > 0:
                    if matrix[i - 1][j - 1] == 56 and matrix[i - 1][j] == 56 and (matrix[i][j - 1] == 56):
                        count += 1
                if i < rows - 1 and j > 0:
                    if matrix[i + 1][j - 1] == 56 and matrix[i + 1][j] == 56 and (matrix[i][j - 1] == 56):
                        count += 1
                if i > 0 and j < cols - 1:
                    if matrix[i - 1][j + 1] == 56 and matrix[i - 1][j] == 56 and (matrix[i][j + 1] == 56):
                        count += 1
                if i < rows - 1 and j < cols - 1:
                    if matrix[i + 1][j + 1] == 56 and matrix[i + 1][j] == 56 and (matrix[i][j + 1] == 56):
                        count += 1
    return count