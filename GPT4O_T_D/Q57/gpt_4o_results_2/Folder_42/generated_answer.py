import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = 862
    rows, columns = matrix.shape
    submatrices = []
    for start_row in range(rows):
        for start_col in range(columns):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, columns):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix)
    return submatrices