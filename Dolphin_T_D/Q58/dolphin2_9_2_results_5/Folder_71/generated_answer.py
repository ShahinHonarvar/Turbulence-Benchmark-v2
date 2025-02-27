import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 78
    num_rows = matrix.shape[0]
    num_cols = matrix.shape[1]
    if num_rows * num_cols < num_elements:
        return 0
    submatrix_count = 0
    for i in range(num_rows - num_elements + 1):
        for j in range(num_cols - num_elements + 1):
            if np.sum(matrix[i:i + num_elements, j:j + num_elements]) == num_elements * 78:
                submatrix_count += 1
    return submatrix_count