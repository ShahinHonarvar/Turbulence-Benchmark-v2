import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    total_elements = row_count * col_count
    if total_elements < 45:
        return 0
    submatrix_count = 0
    for i in range(row_count - 1):
        for j in range(col_count - 1):
            if (i + 1) * (j + 1) >= 45 and (row_count - i) * (col_count - j) >= 45:
                submatrix_count += 1
    return submatrix_count