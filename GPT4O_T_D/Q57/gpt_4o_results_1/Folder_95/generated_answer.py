import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices_with_sum(mat, target):
        row_count = mat.shape[0]
        col_count = mat.shape[1]
        submatrices = []
        for start_row in range(row_count):
            for end_row in range(start_row, row_count):
                for start_col in range(col_count):
                    for end_col in range(start_col, col_count):
                        submatrix = mat[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(submatrix) == target:
                            submatrices.append(submatrix)
        return submatrices
    return all_submatrices_with_sum(np.array(matrix), 19)