import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 20
    for r in range(rows):
        for c in range(cols):
            for r_size in range(1, rows - r + 1):
                for c_size in range(1, cols - c + 1):
                    if r_size * c_size == n:
                        count += 1
    return count