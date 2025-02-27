import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(matrix, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        return np.sum(matrix[top_left_x:bottom_right_x + 1, top_left_y:bottom_right_y + 1])
    submatrices = []
    rows, cols = matrix.shape
    for top_left_x in range(rows):
        for top_left_y in range(cols):
            for bottom_right_x in range(top_left_x, rows):
                for bottom_right_y in range(top_left_y, cols):
                    if get_submatrix_sum(matrix, top_left_x, top_left_y, bottom_right_x, bottom_right_y) == -336:
                        submatrix = matrix[top_left_x:bottom_right_x + 1, top_left_y:bottom_right_y + 1].tolist()
                        submatrices.append(submatrix)
    return submatrices