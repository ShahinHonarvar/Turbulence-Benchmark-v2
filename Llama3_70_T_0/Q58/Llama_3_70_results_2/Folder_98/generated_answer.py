import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 2):
        for col in range(cols - 2):
            submatrix = matrix[row:row + 3, col:col + 3]
            if submatrix.size == 9:
                count += 1
    return count