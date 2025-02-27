import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 103):
        for c in range(cols - 103):
            submatrix = matrix[r:r + 104, c:c + 104]
            if submatrix.size == 104:
                count += 1
    return count