import numpy as np

def submatrix_with_n_numbers(matrix, n=59):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r2 in range(r + 1, rows + 1):
                for c2 in range(c + 1, cols + 1):
                    if len(matrix[r:r2, c:c2].flatten()) == n:
                        count += 1
    return count