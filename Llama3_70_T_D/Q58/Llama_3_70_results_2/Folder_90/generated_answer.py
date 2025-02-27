import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for last_col in range(j, col):
                    submatrix = matrix[i:k + 1, j:last_col + 1]
                    if submatrix.size == 176:
                        count += 1
    return count