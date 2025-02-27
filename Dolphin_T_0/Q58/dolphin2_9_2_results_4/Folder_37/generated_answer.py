import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or (not np.issubdtype(matrix.dtype, np.integer)):
        return 0
    if matrix.size < 64:
        return 0
    shape = (int(matrix.size ** 0.5), int(matrix.size ** 0.5))
    if matrix.shape != shape:
        return 0
    submatrices = 0
    for i in range(matrix.shape[0] - 7):
        for j in range(matrix.shape[1] - 7):
            if np.all(matrix[i:i + 8, j:j + 8] == 64):
                submatrices += 1
    return submatrices