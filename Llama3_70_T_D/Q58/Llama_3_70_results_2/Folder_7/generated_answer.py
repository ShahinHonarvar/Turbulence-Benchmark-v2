import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 121 + 1):
        for col in range(cols - 121 + 1):
            submatrix = matrix[row:row + 121, col:col + 121]
            count += 1
    return count