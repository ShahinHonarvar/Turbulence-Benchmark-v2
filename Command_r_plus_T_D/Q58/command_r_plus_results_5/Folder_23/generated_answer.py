import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 68):
        for j in range(cols - 68):
            submatrix = matrix[i:i + 69, j:j + 69]
            if np.count_nonzero(submatrix) == 69:
                count += 1
    return count