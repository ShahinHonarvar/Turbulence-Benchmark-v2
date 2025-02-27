import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for sub_r in range(r + 1, rows + 1):
                for sub_c in range(c + 1, cols + 1):
                    submatrix = matrix[r:sub_r, c:sub_c]
                    if np.count_nonzero(submatrix == 88) == 88:
                        count += 1
    return count