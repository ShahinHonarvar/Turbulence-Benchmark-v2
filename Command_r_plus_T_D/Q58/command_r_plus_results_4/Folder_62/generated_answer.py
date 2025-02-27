import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 185):
        for j in range(cols - 185):
            submatrix = matrix[i:i + 186, j:j + 186]
            if submatrix.size == 186 ** 2:
                count += 1
    return count