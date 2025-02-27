import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    rows, cols = matrix.shape
    if rows * cols < 15:
        return 0
    count = 0
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    if (x - i + 1) * (y - j + 1) == 15:
                        count += 1
    return count