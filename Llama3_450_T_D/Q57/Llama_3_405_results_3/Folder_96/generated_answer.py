import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        submatrices = []
        for row_start in range(rows):
            for row_end in range(row_start + 1, rows + 1):
                for col_start in range(cols):
                    for col_end in range(col_start + 1, cols + 1):
                        submatrices.append(matrix[row_start:row_end, col_start:col_end])
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == -63]
    return result