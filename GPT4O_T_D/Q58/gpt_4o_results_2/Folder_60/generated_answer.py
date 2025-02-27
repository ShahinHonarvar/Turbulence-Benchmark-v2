import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            for i in range(rows - row + 1):
                for j in range(columns - column + 1):
                    if row * column == 88:
                        count += 1
    return count