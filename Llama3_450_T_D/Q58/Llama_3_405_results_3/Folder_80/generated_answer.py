import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    size = 180
    for row in range(rows):
        for col in range(cols):
            for r in range(row, rows):
                for c in range(col, cols):
                    sub_matrix = matrix[row:r + 1, col:c + 1]
                    if sub_matrix.size == size:
                        count += 1
    return count