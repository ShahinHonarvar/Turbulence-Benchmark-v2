import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    count = 0
    for i in range(row_count):
        for j in range(col_count):
            if matrix[i:i + 5, j:j + 5].size == 186:
                count += 1
    return count