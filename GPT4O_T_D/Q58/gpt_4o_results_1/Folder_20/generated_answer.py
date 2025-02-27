import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows * cols < 49:
        return 0
    count = 0
    for r in range(rows):
        for c in range(cols):
            for size in range(1, min(rows - r, cols - c) + 1):
                if size * size == 49:
                    count += 1
    return count