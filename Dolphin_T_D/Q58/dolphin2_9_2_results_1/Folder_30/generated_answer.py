import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 94
    rows, cols = matrix.shape
    end_row = rows - n + 1
    end_col = cols - n + 1
    for i in range(end_row):
        for j in range(end_col):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                count += 1
    return count