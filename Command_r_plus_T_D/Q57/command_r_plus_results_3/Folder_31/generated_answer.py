import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or (not np.issubdtype(matrix.dtype, np.integer)):
        raise ValueError('Input must be a 2D numpy array of integers.')
    rows, cols = matrix.shape
    target_sum = -44
    result = []
    for i in range(rows):
        for j in range(cols):
            for h in range(i, rows):
                for w in range(j, cols):
                    submatrix = matrix[i:h + 1, j:w + 1]
                    if submatrix.size and submatrix.sum() == target_sum:
                        result.append(submatrix)
    return result