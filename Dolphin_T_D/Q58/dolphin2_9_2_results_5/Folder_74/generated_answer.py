import numpy as np

def submatrix_with_n_numbers(matrix):
    target_size = 48
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 6):
        for j in range(num_cols - 6):
            submatrix = matrix[i:i + 7, j:j + 7]
            if submatrix.size == target_size:
                count += 1
    return count