import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    unique_elements = np.unique(matrix)
    count = 0
    for element in unique_elements:
        if np.sum(matrix == element) == 2:
            count += 1
    return count