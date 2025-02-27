import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 54
    m, n = matrix.shape
    count = 0
    for i in range(m - num_elements + 1):
        for j in range(n - num_elements + 1):
            if np.count_nonzero(matrix[i:i + num_elements, j:j + num_elements]) == num_elements:
                count += 1
    return count