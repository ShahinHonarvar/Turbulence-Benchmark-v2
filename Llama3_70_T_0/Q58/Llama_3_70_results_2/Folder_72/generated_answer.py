import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 3):
        for col in range(cols - 3):
            count += 1
    return count