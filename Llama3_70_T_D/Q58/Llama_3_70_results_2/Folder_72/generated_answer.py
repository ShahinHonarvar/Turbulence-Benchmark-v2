import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows - 3):
        for col in range(cols - 3):
            count += 1
    return count