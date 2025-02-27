import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 36):
        for c in range(cols - 36):
            submatrix = matrix[r:r + 37, c:c + 37]
            if submatrix.size == 37 * 37:
                count += 1
    return count