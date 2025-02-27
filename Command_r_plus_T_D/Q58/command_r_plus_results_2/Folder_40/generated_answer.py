import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    unique, counts = np.unique(matrix, return_counts=True)
    return np.count_nonzero(counts == 1)