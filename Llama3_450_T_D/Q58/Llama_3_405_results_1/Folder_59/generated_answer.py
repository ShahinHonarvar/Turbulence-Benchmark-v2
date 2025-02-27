import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 76
    for r in range(rows):
        for c in range(cols):
            for r_sub in range(r, rows):
                for c_sub in range(c, cols):
                    submatrix = matrix[r:r_sub + 1, c:c_sub + 1]
                    if submatrix.size == n:
                        count += 1
    return count