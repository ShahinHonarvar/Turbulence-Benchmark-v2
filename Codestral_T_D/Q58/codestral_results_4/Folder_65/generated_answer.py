import numpy as np

def submatrix_with_n_numbers(matrix, n=35):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_size in range(r, rows):
                for c_size in range(c, cols):
                    submatrix = matrix[r:r_size + 1, c:c_size + 1]
                    if submatrix.size == n and np.count_nonzero(submatrix == 35) == n:
                        count += 1
    return count