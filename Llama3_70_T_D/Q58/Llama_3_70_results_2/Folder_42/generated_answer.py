import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    n = 193
    for row in range(rows):
        for col in range(cols):
            for size in range(1, min(rows - row, cols - col) + 1):
                if size * size == n:
                    count += 1
    return count