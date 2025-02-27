import numpy as np

def submatrix_with_n_numbers(matrix):
    row_length, col_length = matrix.shape
    count = 0
    for i in range(row_length - 10 + 1):
        for j in range(col_length - 10 + 1):
            if np.count_nonzero(matrix[i:i + 10, j:j + 10]) == 45:
                count += 1
    return count