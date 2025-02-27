import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for end_col in range(j, cols):
                    submatrix = matrix[i:k + 1, j:end_col + 1]
                    if submatrix.size == 103:
                        count += 1
    return count