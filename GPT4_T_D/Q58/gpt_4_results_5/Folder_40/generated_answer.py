import numpy as np

def submatrix_with_n_numbers(matrix):
    counts = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                counts += 1
    return counts