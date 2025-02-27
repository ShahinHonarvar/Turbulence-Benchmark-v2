import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_size = 179
    num_submatrices = 0
    for i in range(row_count - submatrix_size + 1):
        for j in range(col_count - submatrix_size + 1):
            num_submatrices += 1
    return num_submatrices