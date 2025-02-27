import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            if i + 111 <= rows and j + 111 <= cols:
                count += 1
    return count