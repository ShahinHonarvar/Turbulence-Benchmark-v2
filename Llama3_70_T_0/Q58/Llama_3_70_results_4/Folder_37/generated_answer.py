import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 7):
        for col in range(cols - 7):
            submatrix = matrix[row:row + 8, col:col + 8]
            if submatrix.size == 64:
                count += 1
    return count