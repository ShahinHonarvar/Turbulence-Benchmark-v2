import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for r in range(rows):
        for c in range(cols):
            for k in range(1, min(rows - r, cols - c) + 1):
                submatrix = matrix[r:r + k, c:c + k]
                if submatrix.size == 191:
                    count += 1
    return count