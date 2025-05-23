import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 29 + 1):
        for j in range(cols - 29 + 1):
            if i + 29 <= rows and j + 29 <= cols:
                count += 1
    return count