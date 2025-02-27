import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 3):
        for c in range(cols - 5):
            count += 1
    return count