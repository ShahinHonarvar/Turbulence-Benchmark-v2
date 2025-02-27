import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 104
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            if row + n <= rows and col + n <= cols:
                count += 1
    return count