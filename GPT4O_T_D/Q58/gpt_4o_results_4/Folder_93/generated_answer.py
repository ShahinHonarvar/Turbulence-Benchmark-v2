import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for r in range(rows):
        for c in range(cols):
            for dr in range(1, rows - r + 1):
                for dc in range(1, cols - c + 1):
                    if dr * dc == 53:
                        submatrix_count += 1
    return submatrix_count