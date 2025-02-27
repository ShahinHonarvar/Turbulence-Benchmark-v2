import numpy as np

def submatrix_with_n_numbers(matrix, n=13):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows - n + 1):
        for col in range(cols - n + 1):
            count += 1
    return count