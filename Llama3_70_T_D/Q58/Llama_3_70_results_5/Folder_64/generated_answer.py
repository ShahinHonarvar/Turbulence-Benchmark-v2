import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for row in range(rows - 1):
        for col in range(cols - 1):
            submatrix = matrix[row:row + 2, col:col + 2]
            if submatrix.size == 7:
                count += 1
    for row in range(rows - 2):
        for col in range(cols):
            submatrix = matrix[row:row + 3, col]
            if submatrix.size == 7:
                count += 1
    for row in range(rows):
        for col in range(cols - 2):
            submatrix = matrix[row, col:col + 3]
            if submatrix.size == 7:
                count += 1
    for row in range(rows - 1):
        for col in range(cols - 2):
            submatrix = matrix[row:row + 2, col:col + 3]
            if submatrix.size == 7:
                count += 1
    for row in range(rows - 2):
        for col in range(cols - 1):
            submatrix = matrix[row:row + 3, col:col + 2]
            if submatrix.size == 7:
                count += 1
    return count