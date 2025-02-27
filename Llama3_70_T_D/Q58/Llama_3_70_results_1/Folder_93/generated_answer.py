import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for sub_row in range(row + 1, len(matrix) + 1):
                for sub_col in range(col + 1, len(matrix[0]) + 1):
                    submatrix = matrix[row:sub_row, col:sub_col]
                    if submatrix.size == 53:
                        count += 1
    return count