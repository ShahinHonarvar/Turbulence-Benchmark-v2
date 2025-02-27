import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    if matrix.ndim != 2:
        return 0
    if not np.issubdtype(matrix.dtype, np.integer):
        return 0
    shape = matrix.shape
    sub_size = 97
    count = 0
    for i in range(shape[0] - sub_size + 1):
        for j in range(shape[1] - sub_size + 1):
            if matrix[i:i + sub_size, j:j + sub_size].reshape(-1).sum() == sub_size:
                count += 1
    return count