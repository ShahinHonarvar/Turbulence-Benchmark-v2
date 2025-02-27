import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    submatrix_size = int(np.sqrt(43))
    count = 0
    for i in range(n_rows - submatrix_size + 1):
        for j in range(n_cols - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.sum(submatrix) == 43:
                count += 1
    return count