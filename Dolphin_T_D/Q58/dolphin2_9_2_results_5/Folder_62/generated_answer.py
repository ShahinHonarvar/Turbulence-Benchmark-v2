import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    if len(matrix[i:k + 1, j:l + 1].flatten()) == 186:
                        count += 1
    return count