import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_size = 179
    count = 0
    for i in range(rows):
        for j in range(cols):
            submatrix = matrix[i:i + target_size, j:j + target_size]
            if submatrix.size == target_size ** 2:
                count += 1
    return count