import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    submatrix_size = 57
    for r in range(rows):
        for c in range(cols):
            for sub_height in range(1, rows - r + 1):
                sub_width = submatrix_size // sub_height
                if sub_height * sub_width == submatrix_size and c + sub_width <= cols:
                    count += 1
    return count