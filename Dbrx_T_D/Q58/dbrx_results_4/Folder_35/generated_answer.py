import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_rows, n_cols = matrix.shape
    for i in range(n_rows - 2 + 1):
        for j in range(n_cols - 2 + 1):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix == 111) == 9:
                count += 1
    return count