import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_rows, n_cols = matrix.shape
    for i in range(n_rows):
        for j in range(n_cols):
            n = matrix[i:, j:]
            if n.size >= 13:
                count += 1
    return count