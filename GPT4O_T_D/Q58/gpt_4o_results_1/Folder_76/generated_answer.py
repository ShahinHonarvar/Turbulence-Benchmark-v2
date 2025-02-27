import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for s_r in range(r, rows):
                for s_c in range(c, cols):
                    submatrix = matrix[r:s_r + 1, c:s_c + 1]
                    if submatrix.size == 159:
                        count += 1
    return count