import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 174):
        for j in range(n_cols - 174):
            submatrix = matrix[i:i + 175, j:j + 175]
            if np.all(submatrix == 1):
                count += 1
    return count