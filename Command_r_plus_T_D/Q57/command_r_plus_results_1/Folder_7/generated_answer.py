import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input must be a numpy ndarray.')
    if matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional matrix.')
    if not np.issubdtype(matrix.dtype, np.integer):
        raise TypeError('Input matrix must contain only integers.')
    target_sum = -128
    num_rows, num_cols = matrix.shape
    submatrices = []
    for i in range(num_rows):
        for j in range(num_cols):
            for h in range(i, num_rows):
                for w in range(j, num_cols):
                    submatrix = matrix[i:h + 1, j:w + 1]
                    if submatrix.sum() == target_sum:
                        submatrices.append(submatrix)
    return submatrices