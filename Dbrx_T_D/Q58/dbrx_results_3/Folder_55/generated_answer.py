import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 39 + 1):
        for j in range(n_cols - 39 + 1):
            submatrix = matrix[i:i + 39, j:j + 39]
            if np.all(submatrix == 39):
                count += 1
    return count