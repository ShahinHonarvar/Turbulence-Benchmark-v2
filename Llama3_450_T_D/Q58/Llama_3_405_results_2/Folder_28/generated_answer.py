import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 37
    for row_start in range(rows):
        for col_start in range(cols):
            elements = 0
            for row_end in range(row_start, rows):
                elements += cols - col_start
                if elements >= n:
                    break
            else:
                continue
            for col_end in range(col_start, cols):
                submatrix_elements = (row_end - row_start + 1) * (col_end - col_start + 1)
                if submatrix_elements == n:
                    count += 1
    return count