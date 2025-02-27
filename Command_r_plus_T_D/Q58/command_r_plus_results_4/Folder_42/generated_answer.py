import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    n = 193
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.count_nonzero(matrix[i:i + n, j:j + n]) == n:
                count += 1
    return count