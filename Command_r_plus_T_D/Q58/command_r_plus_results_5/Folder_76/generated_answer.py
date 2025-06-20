import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_sum = 159
    count = 0
    for i in range(rows):
        for j in range(cols):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == target_sum:
                count += 1
    return count