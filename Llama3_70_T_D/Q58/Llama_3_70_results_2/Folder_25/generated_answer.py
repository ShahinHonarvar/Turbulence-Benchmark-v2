import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 66
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for i in range(row + n, rows + 1):
                for j in range(col + n, cols + 1):
                    submatrix = matrix[row:i, col:j]
                    if submatrix.size == n * n:
                        count += 1
    return count