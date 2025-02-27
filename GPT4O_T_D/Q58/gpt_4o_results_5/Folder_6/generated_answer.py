import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    total_elements = matrix.size
    count = 0
    for rows in range(1, matrix.shape[0] + 1):
        for cols in range(1, matrix.shape[1] + 1):
            if rows * cols == 122:
                count += (matrix.shape[0] - rows + 1) * (matrix.shape[1] - cols + 1)
    return count