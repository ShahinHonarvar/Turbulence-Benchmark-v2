import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for size in range(1, min(rows, cols) + 1):
        if size * size == 76:
            for row in range(rows - size + 1):
                for col in range(cols - size + 1):
                    submatrix = matrix[row:row + size, col:col + size]
                    count += 1
    return count