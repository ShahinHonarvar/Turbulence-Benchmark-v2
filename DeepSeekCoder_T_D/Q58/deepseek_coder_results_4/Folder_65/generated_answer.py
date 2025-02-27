import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 34):
        for c in range(cols - 34):
            submatrix = matrix[r:r + 35, c:c + 35]
            if submatrix.size == 35 * 35:
                count += 1
    return count