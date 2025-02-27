import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for top_row in range(len(matrix)):
        for left_column in range(len(matrix[0])):
            for bottom_row in range(top_row, len(matrix)):
                for right_column in range(left_column, len(matrix[0])):
                    if np.sum(matrix[top_row:bottom_row + 1, left_column:right_column + 1]) == -15:
                        submatrices.append(matrix[top_row:bottom_row + 1, left_column:right_column + 1])
    return submatrices