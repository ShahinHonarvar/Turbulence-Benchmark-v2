import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_size = 186
    count = 0
    for i in range(rows):
        for j in range(cols):
            submatrix_rows = rows - i
            submatrix_cols = cols - j
            if submatrix_rows * submatrix_cols == target_size:
                count += 1
                break
            elif submatrix_rows * submatrix_cols < target_size:
                break
    return count