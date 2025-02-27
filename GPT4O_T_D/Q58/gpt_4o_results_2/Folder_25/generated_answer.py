import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    nrows, ncols = matrix.shape
    total_elements = 66
    submatrices_count = 0
    for r in range(1, nrows + 1):
        for c in range(1, ncols + 1):
            if r * c == total_elements:
                count_r = nrows - r + 1
                count_c = ncols - c + 1
                submatrices_count += count_r * count_c
    return submatrices_count