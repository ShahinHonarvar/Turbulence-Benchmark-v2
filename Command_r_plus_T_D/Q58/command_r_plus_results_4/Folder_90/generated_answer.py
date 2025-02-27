import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 176
    row_combinations = np.math.comb(row_count, n)
    col_combinations = np.math.comb(col_count, n)
    return row_combinations * col_combinations