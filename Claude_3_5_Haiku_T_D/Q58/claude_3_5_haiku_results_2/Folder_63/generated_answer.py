import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total_count = 0
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if submatrix.size > 0 and np.count_nonzero(submatrix) == 57:
                        total_count += 1
    return total_count