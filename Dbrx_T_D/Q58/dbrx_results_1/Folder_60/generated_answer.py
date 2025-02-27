import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 8
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - n + 1):
        for j in range(n_cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == 88):
                count += 1
    return count