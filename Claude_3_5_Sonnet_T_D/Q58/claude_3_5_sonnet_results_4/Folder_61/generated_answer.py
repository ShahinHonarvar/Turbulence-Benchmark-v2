import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a 2D numpy array')
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if len(np.unique(submatrix)) == 4:
                count += 1
    return count