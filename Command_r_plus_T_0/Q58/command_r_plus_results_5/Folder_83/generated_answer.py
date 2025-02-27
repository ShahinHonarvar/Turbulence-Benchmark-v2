import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 46):
        for j in range(cols - 46):
            submatrix = matrix[i:i + 47, j:j + 47]
            if submatrix.size == 47 * 47:
                count += 1
    return count