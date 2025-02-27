import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 59
    matrix_shape = matrix.shape
    rows = matrix_shape[0]
    cols = matrix_shape[1]
    count = 0
    for x in range(rows - n + 1):
        for y in range(cols - n + 1):
            if np.all(matrix[x:x + n, y:y + n]):
                count += 1
    return count