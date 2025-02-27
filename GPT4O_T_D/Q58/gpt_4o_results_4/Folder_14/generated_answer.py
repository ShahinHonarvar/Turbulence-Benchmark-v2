import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row_count, col_count = matrix.shape
    for r in range(row_count):
        for c in range(col_count):
            for h in range(1, row_count - r + 1):
                for w in range(1, col_count - c + 1):
                    if h * w == 84:
                        count += 1
    return count