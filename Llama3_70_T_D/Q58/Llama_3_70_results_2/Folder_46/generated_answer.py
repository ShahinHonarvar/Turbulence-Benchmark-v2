import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 11):
        for col in range(cols - 11):
            submatrix = matrix[row:row + 12, col:col + 12]
            if submatrix.size == 144:
                count += 1
    return count