import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 7
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            if row + 2 <= rows and col + 2 <= cols:
                submatrix = matrix[row:row + 3, col:col + 3]
                if submatrix.size == n:
                    count += 1
    return count