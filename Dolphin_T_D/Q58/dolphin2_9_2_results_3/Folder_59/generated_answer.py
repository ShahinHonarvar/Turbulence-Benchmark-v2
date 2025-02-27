import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i < rows - 1 and j < cols - 1:
                if matrix[i][j] == 76 or matrix[i][j + 1] == 76 or matrix[i + 1][j] == 76 or (matrix[i + 1][j + 1] == 76):
                    count += 1
    return count