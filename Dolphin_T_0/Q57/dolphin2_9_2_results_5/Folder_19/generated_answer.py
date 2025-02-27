import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix_np = np.array(matrix)
    for top_row in range(len(matrix)):
        for bottom_row in range(top_row, len(matrix)):
            for left_column in range(len(matrix[0])):
                for right_column in range(left_column, len(matrix[0])):
                    sub_matrix = matrix_np[top_row:bottom_row + 1, left_column:right_column + 1]
                    if np.sum(sub_matrix) == -97:
                        result.append(sub_matrix)
    return result if len(result) != 0 else ''