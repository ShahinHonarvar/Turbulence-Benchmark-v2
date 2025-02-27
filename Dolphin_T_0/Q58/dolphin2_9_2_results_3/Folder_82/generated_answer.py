import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    submatrix_count = 0
    for i in range(num_rows - 99):
        for j in range(num_cols - 99):
            submatrix = matrix[i:i + 100, j:j + 100]
            submatrix_count += 1 if np.all(submatrix == 99) else 0
    return submatrix_count