import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 16
    m = 4
    rows, cols = matrix.shape
    for row in range(rows - m + 1):
        for col in range(cols - m + 1):
            submatrix = matrix[row:row + m, col:col + m]
            if submatrix.size == n:
                count += 1
    return count