import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for top_row in range(matrix.shape[0]):
        for bottom_row in range(top_row, matrix.shape[0]):
            for left_column in range(matrix.shape[1]):
                for right_column in range(left_column, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[top_row:bottom_row + 1, left_column:right_column + 1])
                    if submatrix_sum == -452:
                        submatrix = matrix[top_row:bottom_row + 1, left_column:right_column + 1]
                        result.append(submatrix)
    return result