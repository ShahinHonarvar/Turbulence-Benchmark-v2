import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    n = 66
    for r in range(rows):
        for c in range(cols):
            for h in range(1, rows - r + 1):
                for w in range(1, cols - c + 1):
                    submatrix = matrix[r:r + h, c:c + w]
                    if submatrix.size == n:
                        count += 1
    return count