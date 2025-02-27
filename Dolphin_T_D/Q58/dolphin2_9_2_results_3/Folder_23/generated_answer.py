import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for r in range(rows - 2):
        for c in range(cols - 2):
            if matrix[r][c] == 69 and matrix[r + 1][c] == 69 and (matrix[r + 2][c] == 69) and (matrix[r][c + 1] == 69) and (matrix[r + 1][c + 1] == 69) and (matrix[r + 2][c + 1] == 69) and (matrix[r][c + 2] == 69) and (matrix[r + 1][c + 2] == 69) and (matrix[r + 2][c + 2] == 69):
                submatrix_count += 1
    return submatrix_count