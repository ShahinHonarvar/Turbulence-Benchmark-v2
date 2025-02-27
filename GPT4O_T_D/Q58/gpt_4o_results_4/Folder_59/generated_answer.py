import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for dr in range(1, rows - r + 1):
                for dc in range(1, cols - c + 1):
                    if dr * dc == 76:
                        total_count += 1
    return total_count