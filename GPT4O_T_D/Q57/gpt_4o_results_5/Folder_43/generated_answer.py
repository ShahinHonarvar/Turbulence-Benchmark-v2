import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix, start_row, start_col, end_row, end_col):
        submatrices = []
        for r1 in range(start_row, end_row + 1):
            for r2 in range(r1, end_row + 1):
                for c1 in range(start_col, end_col + 1):
                    for c2 in range(c1, end_col + 1):
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        submatrices.append(submatrix)
        return submatrices
    result = []
    n_rows, n_cols = matrix.shape
    all_submatrices = get_submatrices(matrix, 0, 0, n_rows - 1, n_cols - 1)
    for submatrix in all_submatrices:
        if np.sum(submatrix) == -81:
            result.append(submatrix.tolist())
    return result