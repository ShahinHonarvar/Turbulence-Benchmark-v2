import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 7):
        for c in range(cols - 7):
            submatrix = matrix[r:r + 8, c:c + 8]
            if submatrix.size == 64:
                count += 1
    return count