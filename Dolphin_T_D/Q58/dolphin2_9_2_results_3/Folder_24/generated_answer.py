import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 51
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i:i + n, j:j + n].size == n ** 2:
                count += 1
    return count