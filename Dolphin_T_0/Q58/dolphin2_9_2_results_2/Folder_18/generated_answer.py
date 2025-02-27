import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 104
    count = 0
    array_rows, array_cols = matrix.shape
    for i in range(0, array_rows - n + 1):
        for j in range(0, array_cols - n + 1):
            if matrix[i:i + n, j:j + n].sum() == n * n:
                count += 1
    return count