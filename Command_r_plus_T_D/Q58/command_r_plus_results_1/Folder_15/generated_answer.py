import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    unique_elements = np.unique(matrix)
    two_element_submatrices = 0
    for element in unique_elements:
        if np.sum(matrix == element) == 2:
            two_element_submatrices += 1
    return two_element_submatrices