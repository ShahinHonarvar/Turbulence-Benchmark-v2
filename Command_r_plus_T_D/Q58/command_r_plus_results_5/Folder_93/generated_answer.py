import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    total_submatrices = (row_count - 1) * (col_count - 1)
    return total_submatrices