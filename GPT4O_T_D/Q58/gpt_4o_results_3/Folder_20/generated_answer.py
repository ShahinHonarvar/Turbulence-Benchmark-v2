import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2:
        return 0
    n_rows, n_cols = matrix.shape
    submatrix_count = 0
    if n_rows < 7 or n_cols < 7:
        return 0
    for i in range(n_rows - 6):
        for j in range(n_cols - 6):
            submatrix = matrix[i:i + 7, j:j + 7]
            if submatrix.size == 49:
                submatrix_count += 1
    return submatrix_count