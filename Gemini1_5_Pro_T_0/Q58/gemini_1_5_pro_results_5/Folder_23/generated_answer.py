import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 69 + 1):
        for j in range(cols - 69 + 1):
            submatrix = matrix[i:i + 69, j:j + 69]
            if submatrix.size == 69:
                count += 1
    return count