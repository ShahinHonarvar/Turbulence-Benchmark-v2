import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 1):
        for col in range(cols - 1):
            submatrix = matrix[row:row + 2, col:col + 2]
            if submatrix.size == 5:
                count += 1
            submatrix = matrix[row:row + 1, col:col + 2]
            submatrix2 = matrix[row + 1:row + 2, col:col + 2]
            if submatrix.size == 3 and submatrix2.size == 2:
                count += 1
            submatrix = matrix[row:row + 2, col:col + 1]
            submatrix2 = matrix[row:row + 2, col + 1:col + 2]
            if submatrix.size == 3 and submatrix2.size == 2:
                count += 1
    return count