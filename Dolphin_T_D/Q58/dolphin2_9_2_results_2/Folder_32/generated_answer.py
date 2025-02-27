import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for r in range(rows):
        for c in range(cols):
            for endr in range(r, rows):
                for endc in range(c, cols):
                    submatrix = matrix[r:endr + 1, c:endc + 1]
                    if len(submatrix.flatten()) == 103:
                        count += 1
    return count