import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    count = 0
    n = 131
    for r in range(rows):
        for c in range(cols):
            for row_span in range(1, rows - r + 1):
                for col_span in range(1, cols - c + 1):
                    if row_span * col_span == n:
                        count += 1
    return count