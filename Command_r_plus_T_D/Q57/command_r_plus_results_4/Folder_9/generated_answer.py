import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input must be a numpy ndarray.')
    if matrix.ndim != 2:
        raise ValueError('Input must be a 2-dimensional numpy ndarray.')
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows + 1):
                for l in range(j, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size and np.sum(submatrix) == -86:
                        result.append(submatrix)
    return result