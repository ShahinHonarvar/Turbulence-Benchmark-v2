import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 39
    matrix_rows, matrix_cols = matrix.shape
    count = 0
    for i in range(matrix_rows - n + 1):
        for j in range(matrix_cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == 39):
                count += 1
    return count