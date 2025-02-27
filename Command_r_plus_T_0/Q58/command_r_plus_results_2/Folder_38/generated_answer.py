import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 33):
        for j in range(cols - 33):
            submatrix = matrix[i:i + 34, j:j + 34]
            if np.count_nonzero(submatrix) == 34:
                count += 1
    return count