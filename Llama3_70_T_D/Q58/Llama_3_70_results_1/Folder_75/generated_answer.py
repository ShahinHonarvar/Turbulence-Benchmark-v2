import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 80
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        if row + 8 > rows:
            break
        for col in range(cols):
            if col + 10 > cols:
                break
            submatrix = matrix[row:row + 8, col:col + 10]
            if submatrix.size == n:
                count += 1
    return count