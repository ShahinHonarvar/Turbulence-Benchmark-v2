import numpy as np

def submatrix_with_n_numbers(matrix):
    n_numbers = 28
    submatrix_count = 0
    row_count, col_count = matrix.shape
    for i in range(row_count - n_numbers + 1):
        for j in range(col_count - n_numbers + 1):
            submatrix = matrix[i:i + n_numbers, j:j + n_numbers]
            if np.sum(submatrix) == n_numbers:
                submatrix_count += 1
    return submatrix_count