import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    size = 18
    count = 0
    for i in range(rows - size + 1):
        for j in range(cols - size + 1):
            submatrix = matrix[i:i + size, j:j + size]
            if submatrix.size == size:
                count += 1
    return count