import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    total_numbers = np.prod(matrix.shape)
    submatrix_size = 131
    submatrix_count = 0
    if total_numbers < submatrix_size:
        return 0
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if submatrix.size == submatrix_size:
                        submatrix_count += 1
    return submatrix_count