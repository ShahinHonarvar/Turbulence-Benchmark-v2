import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for row_start in range(rows - 1):
        for col_start in range(cols - 1):
            submatrix = matrix[row_start:row_start + 2, col_start:col_start + 2]
            if submatrix.size == 4:
                count += 1
    return count