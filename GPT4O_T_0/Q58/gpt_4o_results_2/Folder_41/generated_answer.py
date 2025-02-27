import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for sub_r in range(r, rows):
                for sub_c in range(c, cols):
                    submatrix = matrix[r:sub_r + 1, c:sub_c + 1]
                    if submatrix.size == 73:
                        count += 1
    return count