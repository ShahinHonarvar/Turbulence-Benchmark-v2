import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            for k in range(i + 1, n_rows + 1):
                for l in range(j + 1, n_cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 29:
                        count += 1
    return count