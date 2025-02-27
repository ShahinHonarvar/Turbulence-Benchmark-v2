import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for h in range(1, rows - r + 1):
                for w in range(1, cols - c + 1):
                    if h * w == 80:
                        count += 1
    return count