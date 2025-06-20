import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_rows = target_cols = int(np.sqrt(47))
    count = 0
    for i in range(rows - target_rows + 1):
        for j in range(cols - target_cols + 1):
            submatrix = matrix[i:i + target_rows, j:j + target_cols]
            if np.count_nonzero(submatrix) == 47:
                count += 1
    return count