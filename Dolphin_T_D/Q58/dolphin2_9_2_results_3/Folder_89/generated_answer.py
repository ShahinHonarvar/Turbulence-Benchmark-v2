import numpy as np

def submatrix_with_n_numbers(matrix, n=18):
    row_count, col_count = matrix.shape
    count = 0
    for i in range(row_count - n + 1):
        for j in range(col_count - n + 1):
            if np.count_nonzero(matrix[i:i + n, j:j + n]) == n ** 2:
                count += 1
    return count