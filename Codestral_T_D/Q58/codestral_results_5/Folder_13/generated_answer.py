import numpy as np

def submatrix_with_n_numbers(matrix, n=175):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_len in range(r, rows):
                for c_len in range(c, cols):
                    submatrix = matrix[r:r_len + 1, c:c_len + 1]
                    if submatrix.size == n and np.all(submatrix == submatrix[0, 0]):
                        count += 1
    return count