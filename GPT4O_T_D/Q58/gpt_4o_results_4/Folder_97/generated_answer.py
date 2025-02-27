import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for subrows in range(i + 1, rows + 1):
                for subcols in range(j + 1, cols + 1):
                    if (subrows - i) * (subcols - j) == 120:
                        count += 1
    return count