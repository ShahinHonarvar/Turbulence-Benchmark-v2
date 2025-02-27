import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_size = 122
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (i + 11) * (j + 11) >= target_size:
                count += 1
    return count