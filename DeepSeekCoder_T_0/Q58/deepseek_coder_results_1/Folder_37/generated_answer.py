import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for start_row in range(rows):
        if start_row + 7 >= rows:
            break
        for start_col in range(cols):
            if start_col + 7 >= cols:
                break
            submatrix = matrix[start_row:start_row + 8, start_col:start_col + 8]
            if submatrix.size == 64:
                count += 1
    return count