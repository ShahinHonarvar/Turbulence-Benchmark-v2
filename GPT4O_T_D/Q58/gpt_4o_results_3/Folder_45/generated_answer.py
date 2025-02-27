import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('The input must be a two-dimensional numpy matrix')
    rows, cols = matrix.shape
    count = 0
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            if sub_rows * sub_cols == 28:
                for row in range(rows - sub_rows + 1):
                    for col in range(cols - sub_cols + 1):
                        count += 1
    return count