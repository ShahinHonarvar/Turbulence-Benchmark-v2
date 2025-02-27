import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for last_col in range(j, cols):
                    submatrix = matrix[i:k + 1, j:last_col + 1]
                    if submatrix.size == 84:
                        count += 1
    return count