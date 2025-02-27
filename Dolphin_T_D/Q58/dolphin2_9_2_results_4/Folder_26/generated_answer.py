import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(row, rows):
                for sub_cols in range(col, cols):
                    n_elements = (sub_rows - row + 1) * (sub_cols - col + 1)
                    if n_elements == 115:
                        count += 1
    return count