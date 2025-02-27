import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 15):
        for c in range(cols - 15):
            submatrix = matrix[r:r + 16, c:c + 16]
            if submatrix.size == 256:
                count += 1
    return count