import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 80
    row_combinations = col_combinations = 0
    for i in range(1, row_count + 1):
        if i * col_count >= n:
            row_combinations += 1
            break
    for j in range(1, col_count + 1):
        if j * row_count >= n:
            col_combinations += 1
            break
    return row_combinations * col_combinations