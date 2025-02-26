import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a 2D numpy array')
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for h in range(i, rows):
                for w in range(j, cols):
                    submatrix = matrix[i:h + 1, j:w + 1]
                    if np.prod(submatrix.shape) == 59:
                        count += 1
    return count