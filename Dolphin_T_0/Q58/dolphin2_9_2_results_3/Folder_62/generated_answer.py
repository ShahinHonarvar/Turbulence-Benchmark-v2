import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total = rows * cols
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (i + 1) * (j + 1) - (i * j == 186):
                count += 1
    return count