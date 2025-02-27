import numpy as np

def submatrix_with_n_numbers(matrix, n=49):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for sr in range(1, rows - r + 1):
                for sc in range(1, cols - c + 1):
                    submatrix = matrix[r:r + sr, c:c + sc]
                    if submatrix.size == n:
                        count += 1
    return count