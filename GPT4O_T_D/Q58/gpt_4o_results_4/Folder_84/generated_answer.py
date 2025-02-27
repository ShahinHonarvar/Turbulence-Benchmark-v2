import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for rs in range(1, rows - r + 1):
                for cs in range(1, cols - c + 1):
                    if rs * cs == 127:
                        count += 1
    return count