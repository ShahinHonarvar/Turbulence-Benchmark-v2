import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 28):
        for c in range(cols - 28):
            submatrix = matrix[r:r + 29, c:c + 29]
            if submatrix.size == 29 * 29:
                count += 1
    return count