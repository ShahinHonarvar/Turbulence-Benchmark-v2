import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for top_row in range(0, rows):
        for bottom_row in range(top_row, rows):
            for left_column in range(0, cols):
                for right_column in range(left_column, cols):
                    submatrix = matrix[top_row:bottom_row + 1, left_column:right_column + 1]
                    if submatrix.sum() == 41:
                        submatrices.append(submatrix)
    return submatrices