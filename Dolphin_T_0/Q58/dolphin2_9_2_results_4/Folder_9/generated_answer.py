import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    sub_matrix = matrix[i:k, j:l]
                    if len(sub_matrix.flatten()) == 33:
                        count += 1
    return count