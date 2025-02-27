import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    submatrix_size = 73
    for r in range(rows):
        for c in range(cols):
            for h in range(1, rows - r + 1):
                for w in range(1, cols - c + 1):
                    if h * w == submatrix_size:
                        count += 1
    return count