import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r1 in range(rows):
        for c1 in range(cols):
            if matrix[r1, c1] != 0:
                for r2 in range(r1, rows):
                    for c2 in range(c1, cols):
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        if np.count_nonzero(submatrix) == 186:
                            count += 1
    return count