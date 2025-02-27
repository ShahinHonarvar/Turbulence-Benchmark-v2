import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 6
    submatrix_count = 0
    rows, cols = matrix.shape
    for row in range(rows - n + 1):
        for col in range(cols - n + 1):
            submatrix = matrix[row:row + n, col:col + n]
            if np.isnan(submatrix).any() or np.all(submatrix == 0):
                continue
            submatrix_count += 1
    return submatrix_count