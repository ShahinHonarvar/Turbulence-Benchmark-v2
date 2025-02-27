import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_sum_equal_to(matrix, target_sum):
        rows, cols = matrix.shape
        all_submatrices = []
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row, rows):
                    for end_col in range(start_col, cols):
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(submatrix) == target_sum:
                            all_submatrices.append(submatrix)
        return all_submatrices
    return find_submatrices_sum_equal_to(matrix, -44)