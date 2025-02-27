import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows):
                for y in range(j + 1, cols):
                    submatrix = matrix[i:x, j:y]
                    if len(submatrix) == 88:
                        count += 1
    return count