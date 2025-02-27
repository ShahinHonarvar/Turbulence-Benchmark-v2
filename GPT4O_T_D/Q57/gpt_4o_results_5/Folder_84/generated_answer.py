import numpy as np

def submatrix_with_particular_sum(matrix):

    def compute_sum(sub):
        return np.sum(sub)

    def generate_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for row_start in range(rows):
            for row_end in range(row_start + 1, rows + 1):
                for col_start in range(cols):
                    for col_end in range(col_start + 1, cols + 1):
                        submatrix = matrix[row_start:row_end, col_start:col_end]
                        submatrices.append(submatrix)
        return submatrices
    submatrices = generate_submatrices(matrix)
    result = [sub for sub in submatrices if compute_sum(sub) == -308]
    return result