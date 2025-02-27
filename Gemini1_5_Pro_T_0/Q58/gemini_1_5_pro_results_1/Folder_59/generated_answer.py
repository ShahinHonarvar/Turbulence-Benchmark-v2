import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 75):
        for j in range(cols - 75):
            submatrix = matrix[i:i + 76, j:j + 76]
            if submatrix.size == 76:
                count += 1
    return count