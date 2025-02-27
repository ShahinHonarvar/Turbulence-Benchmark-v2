import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 63):
        for j in range(cols - 63):
            submatrix = matrix[i:i + 64, j:j + 64]
            if submatrix.size == 64:
                count += 1
    return count