import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 97
    rows, cols = matrix.shape
    for row in range(rows - n + 1):
        for col in range(cols - n + 1):
            submatrix = matrix[row:row + n, col:col + n]
            if submatrix.size == n:
                count += 1
    return count