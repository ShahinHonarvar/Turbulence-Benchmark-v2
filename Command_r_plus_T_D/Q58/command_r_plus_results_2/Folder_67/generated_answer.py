import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 42):
        for j in range(cols - 42):
            submatrix = matrix[i:i + 43, j:j + 43]
            if np.count_nonzero(submatrix) == 43:
                count += 1
    return count