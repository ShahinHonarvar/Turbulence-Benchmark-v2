import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 67):
        for j in range(cols - 67):
            submatrix = matrix[i:i + 68, j:j + 68]
            if submatrix.size == 68 * 68:
                count += 1
    return count