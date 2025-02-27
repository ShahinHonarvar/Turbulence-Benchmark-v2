import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows - 27):
        for col in range(cols - 27):
            submatrix = matrix[row:row + 28, col:col + 28]
            count += 1
    return count