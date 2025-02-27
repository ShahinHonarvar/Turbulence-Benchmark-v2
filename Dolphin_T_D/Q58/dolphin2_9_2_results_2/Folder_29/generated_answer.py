import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 3):
        for j in range(cols - 3):
            if matrix[i, j] == matrix[i + 1, j + 1] == matrix[i + 2, j + 2] == 19 and matrix[i, j + 1] == matrix[i + 1, j] == matrix[i + 2, j + 1] == 19 and (matrix[i, j + 2] == matrix[i + 1, j + 1] == matrix[i + 2, j] == 19):
                count += 1
    return count