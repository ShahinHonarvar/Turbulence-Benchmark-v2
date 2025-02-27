import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_size = 173
    count = 0
    for i in range(rows):
        for j in range(cols):
            submatrix = matrix[i:, j:]
            if submatrix.size == target_size:
                count += 1
            elif submatrix.size < target_size:
                break
    return count