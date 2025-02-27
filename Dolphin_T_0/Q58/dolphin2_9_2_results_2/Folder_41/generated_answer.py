import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr in range(-r, rows - r):
                for dc in range(-c, cols - c):
                    if dr != 0 or dc != 0:
                        row_indices = set(range(r, r + dr + 1)) if dr > 0 else set(range(r + dr, r + 1))
                        col_indices = set(range(c, c + dc + 1)) if dc > 0 else set(range(c + dc, c + 1))
                        submatrix_elements = matrix[list(row_indices)][list(col_indices)]
                        if len(submatrix_elements) == 73 and len(set(submatrix_elements)) == 73:
                            count += 1
    return count