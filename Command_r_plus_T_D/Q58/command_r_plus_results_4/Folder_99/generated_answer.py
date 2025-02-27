import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    n = 146
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (i + 2) * (j + 2) == n:
                count += 1
    return count