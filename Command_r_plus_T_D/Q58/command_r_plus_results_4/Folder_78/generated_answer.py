import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 8):
        for j in range(cols - 8):
            submatrix = matrix[i:i + 9, j:j + 9]
            if np.count_nonzero(submatrix) == 91:
                count += 1
    return count