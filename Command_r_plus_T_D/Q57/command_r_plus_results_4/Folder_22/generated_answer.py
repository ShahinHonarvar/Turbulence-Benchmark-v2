import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or (not np.issubdtype(matrix.dtype, np.integer)):
        raise ValueError('Input must be a 2D numpy array of integers.')
    target_sum = -38
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size and np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix)
    return submatrices