import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_sum = 127
    count = 0
    for submatrix_size in range(1, min(rows, cols) + 1):
        for row_start in range(rows - submatrix_size + 1):
            for col_start in range(cols - submatrix_size + 1):
                submatrix_sum = np.sum(matrix[row_start:row_start + submatrix_size, col_start:col_start + submatrix_size])
                if submatrix_sum == target_sum:
                    count += 1
    return count