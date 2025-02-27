import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 82):
        for j in range(cols - 82):
            submatrix = matrix[i:i + 83, j:j + 83]
            if submatrix.size == 83 * 83:
                count += 1
    return count