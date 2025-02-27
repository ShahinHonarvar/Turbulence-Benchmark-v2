import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 62):
        for j in range(cols - 62):
            submatrix = matrix[i:i + 63, j:j + 63]
            if submatrix.size == 63 ** 2:
                count += 1
    return count