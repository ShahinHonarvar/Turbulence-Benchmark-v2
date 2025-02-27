import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 165):
        for c in range(cols - 165):
            submatrix = matrix[r:r + 166, c:c + 166]
            if submatrix.size == 166 * 166:
                count += 1
    return count