import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for height in range(1, rows - r + 1):
                for width in range(1, cols - c + 1):
                    if height * width == 20:
                        count += 1
    return count