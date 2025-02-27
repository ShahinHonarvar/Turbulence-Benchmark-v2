import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 1):
            submatrix = matrix[i:i + 3, j:j + 2]
            if submatrix.size == 60:
                count += 1
    return count