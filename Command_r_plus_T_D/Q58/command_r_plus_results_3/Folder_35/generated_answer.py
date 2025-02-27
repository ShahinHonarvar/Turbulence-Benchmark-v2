import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 100):
        for j in range(cols - 100):
            submatrix = matrix[i:i + 110, j:j + 110]
            if np.count_nonzero(submatrix) == 111:
                count += 1
    return count