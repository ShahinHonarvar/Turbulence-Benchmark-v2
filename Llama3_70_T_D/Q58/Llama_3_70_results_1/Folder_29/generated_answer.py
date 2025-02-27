import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            if row + 19 <= rows and col + 19 <= cols:
                submatrix = matrix[row:row + 19, col:col + 19]
                if submatrix.size == 19 * 19:
                    count += 1
    return count