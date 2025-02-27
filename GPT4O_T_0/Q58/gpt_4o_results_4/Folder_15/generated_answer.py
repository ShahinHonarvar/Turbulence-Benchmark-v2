import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 1 or cols < 2:
        return 0
    count = 0
    for i in range(rows):
        for j in range(cols - 1):
            count += 1
    return count