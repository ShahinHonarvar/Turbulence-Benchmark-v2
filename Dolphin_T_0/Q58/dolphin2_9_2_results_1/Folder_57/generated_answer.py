import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for i2 in range(i, rows):
                for j2 in range(j, cols):
                    submatrix = matrix[i:i2 + 1, j:j2 + 1]
                    num_elements = submatrix.size
                    if num_elements == 92:
                        count += 1
    return count