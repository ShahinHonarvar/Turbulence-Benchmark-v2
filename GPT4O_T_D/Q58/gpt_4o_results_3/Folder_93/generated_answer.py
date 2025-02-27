import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(x, y, n):
        return (x - n + 1) * (y - n + 1) if x >= n and y >= n else 0
    n = 53
    x, y = matrix.shape
    total_count = 0
    for row_size in range(1, x + 1):
        if row_size > n:
            break
        if n % row_size == 0:
            col_size = n // row_size
            if col_size <= y:
                total_count += count_submatrices_of_size(x, y, row_size) * count_submatrices_of_size(y, x, col_size)
    return total_count