import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 19):
        for j in range(cols - 19):
            submatrix = matrix[i:i + 20, j:j + 20]
            if np.count_nonzero(submatrix) == 20:
                count += 1
    return count