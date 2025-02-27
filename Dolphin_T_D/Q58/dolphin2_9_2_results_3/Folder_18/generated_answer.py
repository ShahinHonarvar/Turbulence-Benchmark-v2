import numpy as np

def submatrix_with_n_numbers(matrix):
    row_sum = np.sum(matrix, axis=1)
    col_sum = np.sum(matrix, axis=0)
    total_count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if row_sum[i] + col_sum[j] - matrix[i][j] == 104:
                total_count += 1
    return total_count