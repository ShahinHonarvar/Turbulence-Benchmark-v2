import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_size = 103
    count = 0
    for i in range(rows - target_size + 1):
        for j in range(cols - target_size + 1):
            submatrix = matrix[i:i + target_size, j:j + target_size]
            if submatrix.size == target_size ** 2:
                count += 1
    return count