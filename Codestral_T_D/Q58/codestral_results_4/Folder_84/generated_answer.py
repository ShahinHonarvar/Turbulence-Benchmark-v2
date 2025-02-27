import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    size = 127
    count = 0
    for r in range(rows - size + 1):
        for c in range(cols - size + 1):
            submatrix = matrix[r:r + size, c:c + size]
            if submatrix.sum() == size ** 2:
                count += 1
    return count