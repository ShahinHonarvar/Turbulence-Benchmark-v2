import numpy as np

def submatrix_with_particular_sum(matrix):
    all_submatrices = []
    for top_row in range(len(matrix)):
        for bottom_row in range(top_row, len(matrix)):
            for left_col in range(len(matrix[0])):
                for right_col in range(left_col, len(matrix[0])):
                    submatrix = matrix[top_row:bottom_row + 1, left_col:right_col + 1]
                    if np.sum(submatrix) == -15:
                        all_submatrices.append(submatrix.tolist())
    return all_submatrices