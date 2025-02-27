import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input must be a numpy ndarray.')
    if matrix.ndim != 2:
        raise ValueError('Input must be a 2D matrix.')
    if not np.issubdtype(matrix.dtype, np.integer):
        raise TypeError('Input matrix must contain integers.')
    target_sum = -57
    num_rows, num_cols = matrix.shape
    submatrices = []
    for row_start in range(num_rows):
        for col_start in range(num_cols):
            for row_end in range(row_start, num_rows):
                for col_end in range(col_start, num_cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if submatrix.sum() == target_sum:
                        submatrices.append(submatrix)
    return submatrices