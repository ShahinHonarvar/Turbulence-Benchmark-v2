import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if j + 4 < cols:
                count += 1
            if i + 4 < rows:
                count += 1
            if i + 4 < rows and j + 4 < cols:
                count += 1
            if i + 4 < rows and j >= 4:
                count += 1
    return count