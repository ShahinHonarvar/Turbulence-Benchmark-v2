import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 178):
        for j in range(cols - 178):
            if i + 179 <= rows and j + 179 <= cols:
                count += 1
    return count