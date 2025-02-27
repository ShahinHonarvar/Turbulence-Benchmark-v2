import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_size = 77
    count = 0
    if rows < 1 or cols < 1 or rows * cols < submatrix_size:
        return 0
    for r in range(rows):
        for c in range(cols):
            for height in range(1, rows - r + 1):
                for width in range(1, cols - c + 1):
                    if height * width == submatrix_size:
                        count += 1
    return count