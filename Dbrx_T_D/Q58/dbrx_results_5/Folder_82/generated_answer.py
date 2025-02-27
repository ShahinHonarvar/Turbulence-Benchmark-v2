import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    n_rows, n_cols = matrix_shape
    for i in range(n_rows - 1):
        for j in range(n_cols - 1):
            submatrix = matrix[i:i + n_numbers, j:j + n_numbers]
            if submatrix.size == n_numbers ** 2 and np.all(submatrix == 99):
                submatrix_count += 1
    return submatrix_count