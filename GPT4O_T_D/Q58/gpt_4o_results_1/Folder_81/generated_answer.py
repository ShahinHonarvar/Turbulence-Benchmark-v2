import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_size = 97
    count = 0
    for r in range(rows):
        for c in range(cols):
            if (r + 1) * (c + 1) == submatrix_size:
                if r < rows and c < cols:
                    count += (rows - r) * (cols - c)
    return count