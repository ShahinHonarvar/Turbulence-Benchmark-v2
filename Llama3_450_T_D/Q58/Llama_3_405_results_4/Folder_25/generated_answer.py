import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 66
    for row in range(rows):
        for col in range(cols):
            for height in range(1, rows - row + 1):
                for width in range(1, cols - col + 1):
                    if height * width == n:
                        submatrix = matrix[row:row + height, col:col + width]
                        count += 1
    return count