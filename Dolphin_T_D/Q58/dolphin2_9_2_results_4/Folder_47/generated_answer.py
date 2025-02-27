import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 90
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.count_nonzero(submatrix == np.nan) == n:
                count += 1
    return count