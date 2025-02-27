import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_sum = 77
    count = 0
    for i in range(rows):
        for j in range(cols):
            submatrix = matrix[i:i + target_sum, j:j + target_sum]
            if submatrix.size == target_sum * target_sum:
                count += 1
    return count