import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 23):
        for j in range(cols - 23):
            submatrix = matrix[i:i + 24, j:j + 24]
            if submatrix.size == 24 * 24:
                count += 1
    return count