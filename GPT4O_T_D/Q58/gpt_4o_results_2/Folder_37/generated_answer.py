import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    if rows * cols < 64:
        return 0
    for row in range(rows):
        for col in range(cols):
            if row + 7 < rows and col + 7 < cols:
                count += 1
    return count