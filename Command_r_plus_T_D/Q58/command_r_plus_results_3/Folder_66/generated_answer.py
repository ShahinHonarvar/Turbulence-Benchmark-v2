import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 39):
        for j in range(cols - 39):
            submatrix = matrix[i:i + 42, j:j + 42]
            if np.all(submatrix.flatten() == 42):
                count += 1
    return count