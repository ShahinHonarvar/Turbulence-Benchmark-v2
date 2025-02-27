import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(columns):
            for row in range(i, rows):
                for col in range(j, columns):
                    if len(matrix[i:row + 1, j:col + 1].flat) == 69:
                        count += 1
    return count