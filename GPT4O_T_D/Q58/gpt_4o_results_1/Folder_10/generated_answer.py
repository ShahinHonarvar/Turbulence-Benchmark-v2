import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target = 56
    count = 0
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if (bottom - top + 1) * (right - left + 1) == target:
                        count += 1
    return count