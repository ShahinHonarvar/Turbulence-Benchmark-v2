import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 1, 0, -1):
        for j in range(cols - 1, 0, -1):
            if (i + 1) * (j + 1) == 146:
                count += 1
    return count