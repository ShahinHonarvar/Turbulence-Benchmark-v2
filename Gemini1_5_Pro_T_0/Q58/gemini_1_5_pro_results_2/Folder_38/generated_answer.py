import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 33):
        for j in range(cols - 33):
            for k in range(i + 1, rows - 32):
                for l in range(j + 1, cols - 32):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 34:
                        count += 1
    return count