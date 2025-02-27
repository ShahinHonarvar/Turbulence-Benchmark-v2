import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input must be a numpy ndarray.')
    if len(matrix.shape) != 2:
        raise ValueError('Input must be a 2-dimensional matrix.')
    if not np.issubdtype(matrix.dtype, np.integer):
        raise TypeError('Matrix elements must be integers.')
    target_sum = -77
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix)
    return submatrices