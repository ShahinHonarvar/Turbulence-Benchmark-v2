import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    size = 126
    for r in range(rows):
        for c in range(cols):
            for sub_r in range(r, rows):
                for sub_c in range(c, cols):
                    sub_matrix = matrix[r:sub_r + 1, c:sub_c + 1]
                    if sub_matrix.size == size:
                        count += 1
    return count