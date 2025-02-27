import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 193
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for sub_row in range(i, rows):
                for sub_col in range(j, cols):
                    submatrix = matrix[i:sub_row + 1, j:sub_col + 1]
                    if submatrix.size == n:
                        count += 1
    return count