import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            n_rows = min(matrix.shape[0] - i, 10)
            n_cols = min(matrix.shape[1] - j, 12)
            submatrix = matrix[i:i + n_rows, j:j + n_cols]
            if np.linalg.matrix_rank(submatrix) == 120:
                count += 1
    return count