import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    submatrices_16 = 0
    if rows < 4 or cols < 4:
        return 0
    for i in range(rows - 3):
        for j in range(cols - 3):
            submatrices_16 += 1
    return submatrices_16