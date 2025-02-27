import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 1):
        for c in range(cols - 1):
            submatrix_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
            if submatrix_sum == 175 * 4:
                count += 1
    return count