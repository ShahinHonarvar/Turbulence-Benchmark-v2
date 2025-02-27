import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 38
    for r in range(rows):
        for c in range(cols):
            for r_end in range(r + 1, rows + 1):
                for c_end in range(c + 1, cols + 1):
                    submat = matrix[r:r_end, c:c_end]
                    if submat.size == n:
                        count += 1
    return count