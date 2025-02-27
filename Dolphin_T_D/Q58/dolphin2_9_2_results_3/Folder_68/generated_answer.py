import numpy as np

def submatrix_with_n_numbers(matrix, num=74):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    height, width = matrix.shape
    count = 0
    for i in range(height):
        for j in range(width):
            for i2 in range(i, height):
                for j2 in range(j, width):
                    if (i2 - i + 1) * (j2 - j + 1) == num:
                        count += 1
    return count