import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 8):
        for c in range(cols - 8):
            submatrix = matrix[r:r + 9, c:c + 9]
            if submatrix.size == 81:
                count += 1
    return count