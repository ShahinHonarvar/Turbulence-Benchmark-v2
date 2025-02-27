import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 9):
        for j in range(cols - 17):
            submatrix = matrix[i:i + 10, j:j + 18]
            if submatrix.size == 180:
                count += 1
    return count