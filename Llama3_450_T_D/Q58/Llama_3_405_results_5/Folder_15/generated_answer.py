import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for r in range(rows):
        for c in range(cols):
            for r_sub in range(r, rows):
                for c_sub in range(c, cols):
                    submatrix = matrix[r:r_sub + 1, c:c_sub + 1]
                    if np.count_nonzero(submatrix) == 2:
                        count += 1
    return count