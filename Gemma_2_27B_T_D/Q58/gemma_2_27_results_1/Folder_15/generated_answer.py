import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 1 < rows and j + 1 < cols:
                count += 1
    return count