import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 9):
        for c in range(cols - 17):
            submatrix = matrix[r:r + 10, c:c + 18]
            if submatrix.size == 180:
                count += 1
    return count