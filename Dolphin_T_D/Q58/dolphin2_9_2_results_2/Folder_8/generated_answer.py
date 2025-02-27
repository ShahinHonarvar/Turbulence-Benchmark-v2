import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows = matrix.shape[0]
    num_cols = matrix.shape[1]
    count = 0
    for i in range(num_rows):
        for j in range(num_cols - 1):
            for k in range(i, num_rows):
                if len(matrix[i:k + 1, j:j + 2]) == 29:
                    count += 1
    return count