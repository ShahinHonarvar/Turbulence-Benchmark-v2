import numpy as np

def submatrix_with_n_numbers(matrix, n=176):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == n:
                count += 1
    return count * (rows * cols)