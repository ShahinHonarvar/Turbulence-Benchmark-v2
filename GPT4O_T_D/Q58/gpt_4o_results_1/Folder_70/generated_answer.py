import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 173
    count = 0
    for i1 in range(rows):
        for i2 in range(i1, rows):
            for j1 in range(cols):
                for j2 in range(j1, cols):
                    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
                    if submatrix.size == target_count:
                        count += 1
    return count