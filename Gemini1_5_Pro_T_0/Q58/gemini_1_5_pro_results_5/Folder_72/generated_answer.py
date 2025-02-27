import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 3):
        for j in range(cols - 3):
            if i + 4 <= rows and j + 4 <= cols:
                count += 1
    return count