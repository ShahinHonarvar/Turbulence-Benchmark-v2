import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 40
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            for r_size in range(1, rows - row + 1):
                for c_size in range(1, cols - col + 1):
                    if r_size * c_size == n:
                        count += 1
    return count