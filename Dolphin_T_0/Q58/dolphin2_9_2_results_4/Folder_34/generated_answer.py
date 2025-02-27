import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 83
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 0:
                for x in range(i + 1, rows):
                    for y in range(j + 1, cols):
                        submatrix = matrix[i:x, j:y]
                        if len(submatrix.flatten()) == n:
                            count += 1
    return count