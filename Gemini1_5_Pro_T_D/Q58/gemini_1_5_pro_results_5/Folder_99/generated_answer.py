import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 145):
        for j in range(cols - 145):
            count += 1
    return count