import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_sum = 154
    count = 0
    for i in range(rows):
        for j in range(cols):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.size == 4 and np.sum(submatrix) == target_sum:
                count += 1
    return count