import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 32):
        for c in range(cols - 32):
            submatrix = matrix[r:r + 33, c:c + 33]
            if submatrix.size == 33 * 33:
                count += 1
    return count