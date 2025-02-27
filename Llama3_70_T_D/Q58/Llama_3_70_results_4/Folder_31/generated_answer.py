import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 45
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            max_row = rows - row
            max_col = cols - col
            for size in range(min(max_row, max_col), 0, -1):
                if size * size >= n:
                    submatrix = matrix[row:row + size, col:col + size]
                    if len(submatrix.flatten()) == n:
                        count += 1
    return count