import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    if row_count * col_count < 191:
        return 0

    def count_submatrices_with_n_elements(n):
        count = 0
        for row_start in range(row_count):
            for row_end in range(row_start, row_count):
                for col_start in range(col_count):
                    for col_end in range(col_start, col_count):
                        if (row_end - row_start + 1) * (col_end - col_start + 1) == n:
                            count += 1
        return count
    return count_submatrices_with_n_elements(191)