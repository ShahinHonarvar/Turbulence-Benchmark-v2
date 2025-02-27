import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 102):
        for c in range(cols - 102):
            submatrix = matrix[r:r + 103, c:c + 103]
            if submatrix.size == 103 * 103:
                count += 1
    return count