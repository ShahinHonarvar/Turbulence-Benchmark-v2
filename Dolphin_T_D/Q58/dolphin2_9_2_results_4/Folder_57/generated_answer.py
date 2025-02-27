import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 2):
        for c in range(cols - 2):
            if matrix[r][c] == 92 and matrix[r + 1][c] == 92 and (matrix[r + 2][c] == 92) and (matrix[r][c + 1] == 92) and (matrix[r + 1][c + 1] == 92) and (matrix[r + 2][c + 1] == 92) and (matrix[r][c + 2] == 92) and (matrix[r + 1][c + 2] == 92) and (matrix[r + 2][c + 2] == 92):
                count += 1
    return count