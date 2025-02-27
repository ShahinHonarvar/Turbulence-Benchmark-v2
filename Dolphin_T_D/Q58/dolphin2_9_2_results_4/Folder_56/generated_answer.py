import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 7):
        for j in range(n - 8):
            submatrix_elements = matrix[i:i + 8, j:j + 8]
            if np.count_nonzero(submatrix_elements == 68) == 64:
                count += 1
    return count