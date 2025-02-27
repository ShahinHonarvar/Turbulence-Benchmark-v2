import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    n_numbers = 3
    count = 0
    for i in range(n_rows - n_numbers + 1):
        for j in range(n_cols - n_numbers + 1):
            submatrix = matrix[i:i + n_numbers, j:j + n_numbers]
            if np.count_nonzero(submatrix == 33) == n_numbers * n_numbers:
                count += 1
    return count