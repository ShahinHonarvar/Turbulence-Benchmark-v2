import numpy as np

def submatrix_with_n_numbers(matrix):
    col_sums = np.sum(matrix, axis=0)
    count = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            submatrix_sums = np.sum(matrix[i:j + 1, :], axis=0)
            if (col_sums == submatrix_sums).sum() == len(col_sums):
                count += 1
    return count