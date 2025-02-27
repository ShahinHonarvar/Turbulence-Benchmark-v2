import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 79):
        for j in range(cols - 79):
            submatrix = matrix[i:i + 80, j:j + 80]
            if submatrix.size == 80 * 80:
                count += 1
    return count