import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 114):
        for j in range(cols - 114):
            submatrix = matrix[i:i + 115, j:j + 115]
            if submatrix.size == 115 ** 2:
                count += 1
    return count