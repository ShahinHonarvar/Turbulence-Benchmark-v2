import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    rows, cols = matrix.shape
    for i in range(rows - 2 + 1):
        for j in range(cols - 6 + 1):
            submatrix = matrix[i:i + 3, j:j + 7]
            if np.isin(submatrix, [63]).all():
                total_count += 1
    return total_count