import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or (not np.issubdtype(matrix.dtype, np.integer)):
        raise ValueError('Input must be a 2D numpy integer array.')
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 1:
                submatrix = matrix[i:i + 1, j:j + 1]
                submatrices.append(submatrix)
    return submatrices