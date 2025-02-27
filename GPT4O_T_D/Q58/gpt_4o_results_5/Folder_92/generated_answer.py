import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 3):
            count += 1
    for i in range(rows - 3):
        for j in range(cols - 1):
            count += 1
    for i in range(rows - 1):
        for j in range(cols - 1):
            count += 1
    if rows > 1 and cols > 1:
        for i in range(rows - 3):
            for j in range(cols - 3):
                count += 1
    return count