import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    count = 0
    for i in range(row_count):
        for j in range(col_count):
            for h in range(i, row_count):
                for k in range(j, col_count):
                    submatrix_size = (h - i + 1) * (k - j + 1)
                    if submatrix_size == 67:
                        count += 1
    return count