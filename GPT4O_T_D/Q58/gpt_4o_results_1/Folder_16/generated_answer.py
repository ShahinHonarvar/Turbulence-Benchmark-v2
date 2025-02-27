import numpy as np

def submatrix_with_n_numbers(mat):
    if not isinstance(mat, np.ndarray) or len(mat.shape) != 2:
        return 0
    rows, cols = mat.shape
    total_elements = rows * cols
    if total_elements < 154:
        return 0

    def count_submatrices(current_rows, current_cols):
        return (rows - current_rows + 1) * (cols - current_cols + 1)
    submatrices_count = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r * c == 154:
                submatrices_count += count_submatrices(r, c)
    return submatrices_count