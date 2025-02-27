import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix) + 1):
            for start_row in range(row):
                for start_col in range(col):
                    submatrix = matrix[start_row:col, start_col:start_row:-1]
                    if submatrix.sum() == 13:
                        results.append((start_row, start_col, col - 1, row - 1))
    return results