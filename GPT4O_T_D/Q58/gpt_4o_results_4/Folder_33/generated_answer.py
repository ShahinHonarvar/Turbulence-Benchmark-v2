import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 118
    m, n = matrix.shape
    count = 0
    for row_start in range(m):
        for col_start in range(n):
            for row_end in range(row_start, m):
                for col_end in range(col_start, n):
                    submatrix_size = (row_end - row_start + 1) * (col_end - col_start + 1)
                    if submatrix_size == num_elements:
                        count += 1
    return count