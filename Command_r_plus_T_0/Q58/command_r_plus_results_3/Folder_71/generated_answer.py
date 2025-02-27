import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_sum = 78
    count = 0
    for i in range(rows):
        for j in range(cols):
            submatrix = matrix[i:, j:]
            if submatrix.size == target_sum:
                count += 1
                break
    return count