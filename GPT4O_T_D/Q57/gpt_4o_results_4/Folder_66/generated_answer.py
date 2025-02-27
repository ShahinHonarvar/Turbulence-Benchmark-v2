import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        sub_matrices = []
        for row_start in range(rows):
            for row_end in range(row_start + 1, rows + 1):
                for col_start in range(cols):
                    for col_end in range(col_start + 1, cols + 1):
                        sub_matrices.append(mat[row_start:row_end, col_start:col_end])
        return sub_matrices
    sub_matrices = get_submatrices(matrix)
    result = [sub_matrix for sub_matrix in sub_matrices if np.sum(sub_matrix) == 99]
    return result