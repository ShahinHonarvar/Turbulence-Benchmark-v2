import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 98):
        for j in range(cols - 98):
            submatrix = matrix[i:i + 99, j:j + 99]
            if submatrix.size == 99 * 99:
                count += 1
    return count