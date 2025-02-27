import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 63
    submatrix_count = 0
    m, n = matrix.shape
    for i in range(m - num_elements + 1):
        for j in range(n - num_elements + 1):
            if np.prod(matrix[i:i + num_elements, j:j + num_elements]) == num_elements:
                submatrix_count += 1
    return submatrix_count