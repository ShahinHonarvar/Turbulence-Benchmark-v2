import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input must be a 2-dimensional numpy array.')
    if not np.issubdtype(matrix.dtype, np.integer):
        raise ValueError('Input array must contain integers.')
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows + 1):
                for l in range(j, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size > 0 and np.sum(submatrix) == -86:
                        result.append(submatrix)
    return result