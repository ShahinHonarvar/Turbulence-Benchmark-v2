import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 191
    rows, cols = matrix.shape
    for row in range(rows - int(n ** 0.5) + 1):
        for col in range(cols - int(n ** 0.5) + 1):
            for size in range(int(n ** 0.5), min(rows - row, cols - col) + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if submatrix.size == n:
                    count += 1
    return count