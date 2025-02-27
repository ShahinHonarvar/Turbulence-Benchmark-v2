import numpy as np

def submatrix_with_n_numbers(n_matrix):
    row, col = n_matrix.shape
    submatrix_count = 0
    for i in range(row):
        for j in range(col):
            if (row - i) * (col - j) >= 144:
                submatrix_sum = np.sum(n_matrix[i:i + 12, j:j + 12])
                if submatrix_sum == 144:
                    submatrix_count += 1
    return submatrix_count