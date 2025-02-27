import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    num_elements = 131
    n, m = matrix.shape
    for i in range(n - num_elements + 1):
        for j in range(m - num_elements + 1):
            if np.all(matrix[i:i + num_elements, j:j + num_elements] == num_elements):
                count += 1
    return count