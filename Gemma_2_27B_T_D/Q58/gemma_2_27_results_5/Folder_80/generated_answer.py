import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            submatrix = matrix[i:i + 180 // n_cols, j:j + 180 % n_cols]
            if submatrix.size == 180:
                count += 1
    return count