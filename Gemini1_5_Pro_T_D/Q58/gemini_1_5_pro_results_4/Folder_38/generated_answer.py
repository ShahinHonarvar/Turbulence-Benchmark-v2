import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 33):
            submatrix = matrix[i:i + 1, j:j + 34]
            if submatrix.size == 34:
                count += 1
    return count