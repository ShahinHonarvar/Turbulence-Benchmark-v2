import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 21:
                matrix_dim = min(rows - i + 1, cols - j + 1)
                if matrix_dim >= 3:
                    count += 1
    return count