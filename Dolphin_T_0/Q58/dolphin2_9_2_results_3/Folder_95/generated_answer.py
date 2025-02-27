import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    if matrix.ndim != 2:
        return 0
    dimensions = matrix.shape
    if dimensions[0] < 1 or dimensions[1] < 1:
        return 0
    n = 87
    count = 0
    for i in range(dimensions[0] - n + 1):
        for j in range(dimensions[1] - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                count += 1
    return count