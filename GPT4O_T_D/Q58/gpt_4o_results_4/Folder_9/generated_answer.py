import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            for i_len in range(1, rows - i + 1):
                for j_len in range(1, cols - j + 1):
                    if i_len * j_len == 33:
                        submatrix_count += 1
    return submatrix_count