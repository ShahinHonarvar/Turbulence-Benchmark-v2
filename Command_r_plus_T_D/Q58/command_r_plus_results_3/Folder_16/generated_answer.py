import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 153):
        for j in range(cols - 153):
            submatrix = matrix[i:i + 154, j:j + 154]
            if submatrix.size == 154 * 154:
                count += 1
    return count