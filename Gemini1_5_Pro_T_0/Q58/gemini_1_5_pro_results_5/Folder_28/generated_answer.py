import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 36):
        for j in range(cols - 36):
            submatrix = matrix[i:i + 37, j:j + 37]
            if submatrix.size == 37:
                count += 1
    return count