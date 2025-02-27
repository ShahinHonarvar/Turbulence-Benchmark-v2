import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 106):
        for c in range(cols - 106):
            submatrix = matrix[r:r + 107, c:c + 107]
            if submatrix.size == 107 * 107:
                count += 1
    return count