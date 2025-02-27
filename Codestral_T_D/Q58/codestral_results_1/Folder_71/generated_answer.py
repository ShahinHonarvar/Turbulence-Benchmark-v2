import numpy as np

def submatrix_with_n_numbers(matrix, n=78):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for s in range(1, rows - r + 1):
                for t in range(1, cols - c + 1):
                    submatrix = matrix[r:r + s, c:c + t]
                    if submatrix.size == n:
                        count += 1
    return count