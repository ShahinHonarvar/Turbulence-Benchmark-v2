import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 154
    submatrix_count = 0
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.isin(submatrix, 154).sum() == n ** 2:
                submatrix_count += 1
    return submatrix_count