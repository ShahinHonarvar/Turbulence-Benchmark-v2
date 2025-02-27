import numpy as np

def submatrix_with_n_numbers(matrix):
    n_elements = 49
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(0, rows - n_elements + 1):
        for j in range(0, cols - n_elements + 1):
            submatrix = matrix[i:i + n_elements, j:j + n_elements]
            if np.size(submatrix) == n_elements:
                submatrix_count += 1
    return submatrix_count