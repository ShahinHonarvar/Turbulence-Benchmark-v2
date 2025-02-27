import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    sub_matrix_size = 77
    for r in range(rows):
        for c in range(cols):
            for sub_r in range(r + 1, rows + 1):
                for sub_c in range(c + 1, cols + 1):
                    if (sub_r - r) * (sub_c - c) == sub_matrix_size:
                        count += 1
    return count