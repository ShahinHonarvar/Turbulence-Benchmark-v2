import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for row in range(n_rows - 7):
        for col in range(n_cols - 7):
            submatrix = matrix[row:row + 8, col:col + 8]
            if np.all(submatrix == 48):
                count += 1
    return count