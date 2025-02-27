import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(n - 3):
        for j in range(m - 3):
            submatrix_elements = matrix[i:i + 4, j:j + 4].flatten()
            if np.count_nonzero(submatrix_elements == 39) == 4:
                count += 1
    return count