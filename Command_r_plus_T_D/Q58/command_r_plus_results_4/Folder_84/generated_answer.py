import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows - 126):
        for j in range(cols - 126):
            submatrix = matrix[i:i + 127, j:j + 127]
            if np.count_nonzero(submatrix) == 127:
                submatrix_count += 1
    return submatrix_count