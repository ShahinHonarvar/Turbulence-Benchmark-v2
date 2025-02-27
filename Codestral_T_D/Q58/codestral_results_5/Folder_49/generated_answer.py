import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows - 5):
        for j in range(cols - 12):
            if matrix[i:i + 6, j:j + 12].size == 72:
                submatrix_count += 1
    return submatrix_count