import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows - 4):
        for j in range(cols - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if submatrix.size == 5 * 5:
                submatrix_count += 1
    return submatrix_count