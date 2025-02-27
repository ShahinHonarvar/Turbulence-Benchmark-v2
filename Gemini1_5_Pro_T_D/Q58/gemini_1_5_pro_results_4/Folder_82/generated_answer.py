import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for row_start in range(rows - 99 + 1):
        for col_start in range(cols - 99 + 1):
            if row_start + 99 <= rows and col_start + 99 <= cols:
                count += 1
    return count