import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_size = 72
    count = 0
    for i in range(rows):
        for j in range(cols):
            remaining_rows = rows - i
            remaining_cols = cols - j
            if remaining_rows * remaining_cols >= target_size:
                submatrix_size = remaining_rows * remaining_cols
                count += 1
                break
    return count