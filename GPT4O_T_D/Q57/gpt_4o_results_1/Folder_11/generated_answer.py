import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum):
        n_rows, n_cols = matrix.shape
        submatrices = []
        for start_row in range(n_rows):
            for start_col in range(n_cols):
                for end_row in range(start_row, n_rows):
                    for end_col in range(start_col, n_cols):
                        sub_matrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(sub_matrix) == target_sum:
                            submatrices.append(sub_matrix.tolist())
        return submatrices
    return find_submatrices(matrix, 38)