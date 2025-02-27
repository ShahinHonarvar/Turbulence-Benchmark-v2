import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def count_submatrices(r, c):
        max_rows = min(rows - r, 39)
        max_cols = min(cols - c, 39)
        total = 0
        for sub_r in range(1, max_rows + 1):
            for sub_c in range(1, max_cols + 1):
                if sub_r * sub_c == 39:
                    total += (rows - r - sub_r + 1) * (cols - c - sub_c + 1)
        return total
    for r in range(rows):
        for c in range(cols):
            count += count_submatrices(r, c)
    return count