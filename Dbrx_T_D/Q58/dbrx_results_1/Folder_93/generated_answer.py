import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    dims = matrix.ndim
    if dims != 2:
        return submatrix_count
    height, width = matrix.shape
    for i in range(height - 2 + 1):
        for j in range(width - 2 + 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.isin(53, submatrix).sum() == 4:
                submatrix_count += 1
    return submatrix_count