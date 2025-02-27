import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 126
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    if (k - i + 1) * (l - j + 1) == num_elements:
                        count += 1
    return count