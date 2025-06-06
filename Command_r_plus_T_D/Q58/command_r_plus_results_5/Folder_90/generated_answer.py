import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_sum = 176
    count = 0
    for i in range(rows - 3):
        for j in range(cols - 3):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == target_sum:
                count += 1
    return count