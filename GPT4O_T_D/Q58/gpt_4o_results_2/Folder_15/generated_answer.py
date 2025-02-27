import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 2 or cols < 1:
        return 0
    count = 0
    for i in range(rows - 1):
        for j in range(cols):
            count += 1
    return count