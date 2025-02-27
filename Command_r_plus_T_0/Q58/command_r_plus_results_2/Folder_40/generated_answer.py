import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_sums = np.sum(matrix, axis=1)
    return np.sum(np.where(row_sums == 1, 1, 0))