import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 4):
        for c in range(cols - 5):
            submatrix = matrix[r:r + 5, c:c + 6]
            if submatrix.size == 24:
                count += 1
    return count