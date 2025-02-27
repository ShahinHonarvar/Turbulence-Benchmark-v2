import numpy as np

def submatrix_with_n_numbers(matrix, n=21):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for size in range(1, min(rows - row, cols - col) + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if submatrix.size == n:
                    count += 1
    return count