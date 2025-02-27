import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 139
    count = 0
    for i in range(rows):
        for j in range(cols):
            for subrows in range(1, rows - i + 1):
                for subcols in range(1, cols - j + 1):
                    if subrows * subcols == n:
                        count += 1
    return count