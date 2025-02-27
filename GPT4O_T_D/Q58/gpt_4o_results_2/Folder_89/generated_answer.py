import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for sub_r in range(r, rows):
                for sub_c in range(c, cols):
                    submatrix = matrix[r:sub_r + 1, c:sub_c + 1]
                    if submatrix.size == 18:
                        count += 1
    return count