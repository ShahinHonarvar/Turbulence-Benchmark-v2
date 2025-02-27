import numpy as np

def submatrix_with_n_numbers(matrix):
    row, column = matrix.shape
    count = 0
    for i in range(row):
        for j in range(column):
            for k in range(i + 1, row):
                for l in range(j + 1, column):
                    if len(matrix[i:k + 1, j:l + 1].flatten()) == 95:
                        count += 1
    return count