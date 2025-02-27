import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for h in range(1, rows - i + 1):
                for w in range(1, cols - j + 1):
                    if h * w == 20:
                        count += 1
    return count