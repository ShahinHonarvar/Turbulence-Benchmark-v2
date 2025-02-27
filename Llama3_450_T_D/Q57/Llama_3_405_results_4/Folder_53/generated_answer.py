import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = -37
    submatrices = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for sub_row in range(row, len(matrix)):
                for sub_col in range(col, len(matrix[0])):
                    submatrix = matrix[row:sub_row + 1, col:sub_col + 1]
                    if np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix)
    return submatrices