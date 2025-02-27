import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    if matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional matrix')
    submatrices = []
    rows, cols = matrix.shape
    for h in range(rows):
        for w in range(cols):
            for end_row in range(h + 1, rows + 1):
                for end_col in range(w + 1, cols + 1):
                    submatrix = matrix[h:end_row, w:end_col]
                    if np.sum(submatrix) == 16:
                        submatrices.append(submatrix)
    return submatrices