import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows - 33):
        for j in range(cols - 33):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    if len(matrix[i:k, j:l].flatten()) == 34:
                        count += 1
    return count