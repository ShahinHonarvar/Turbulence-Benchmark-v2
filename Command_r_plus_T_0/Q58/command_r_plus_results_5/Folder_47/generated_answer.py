import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 89):
        for j in range(cols - 89):
            submatrix = matrix[i:i + 90, j:j + 90]
            if submatrix.size == 90 * 90:
                count += 1
    return count