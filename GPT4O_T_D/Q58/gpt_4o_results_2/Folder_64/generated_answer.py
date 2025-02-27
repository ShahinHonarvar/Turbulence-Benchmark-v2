import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    if rows * cols < 7:
        return 0
    count = 0
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submatrix_size = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if submatrix_size == 7:
                        count += 1
    return count