import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 78
    for row in range(rows):
        for col in range(cols):
            for r in range(row + 1, rows + 1):
                for c in range(col + 1, cols + 1):
                    if (r - row) * (c - col) == n:
                        count += 1
    return count