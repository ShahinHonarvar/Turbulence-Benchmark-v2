import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input must be a two-dimensional numpy array')
    rows, cols = matrix.shape
    submatrices = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    submatrix = matrix[start_row:end_row, start_col:end_col]
                    if np.sum(submatrix) == -63:
                        submatrices.append(submatrix)
    return submatrices