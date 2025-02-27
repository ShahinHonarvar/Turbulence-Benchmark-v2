import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            if matrix[i:i + 2, j:j + 2].flatten().size == 38:
                count += 1
    return count