import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    count = 0
    for start_i in range(row_count):
        for start_j in range(col_count):
            for end_i in range(start_i, row_count):
                for end_j in range(start_j, col_count):
                    submatrix_size = (end_i - start_i + 1) * (end_j - start_j + 1)
                    if submatrix_size == 60:
                        count += 1
    return count