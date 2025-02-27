import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for last_col in range(j, cols):
                    submatrix = matrix[i:k + 1, j:last_col + 1]
                    if submatrix.size == 91:
                        count += 1
    return count