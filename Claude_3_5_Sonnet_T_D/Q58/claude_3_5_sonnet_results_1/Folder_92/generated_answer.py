import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a 2D numpy array')
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    submatrix = matrix[i:r + 1, j:c + 1]
                    if submatrix.size == 8:
                        count += 1
    return count