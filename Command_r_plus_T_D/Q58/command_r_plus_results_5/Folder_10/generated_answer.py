import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    total_elements = row_count * col_count
    if total_elements < 56:
        return 0
    count = 0
    for i in range(row_count):
        for j in range(col_count):
            if (i + 2) * (j + 2) >= 56:
                count += 1
                break
    return count