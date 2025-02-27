import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 1 < rows and j + 3 < cols:
                if matrix[i][j] == 40 and matrix[i + 1][j + 1] == 40 and (matrix[i + 2][j + 2] == 40) and (matrix[i + 3][j + 3] == 40):
                    count += 1
    return count