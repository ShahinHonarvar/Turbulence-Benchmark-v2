import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_valid_submatrix(i, j, sub_rows, sub_columns):
        submatrix = matrix[i:i + sub_rows, j:j + sub_columns]
        return np.sum(submatrix) == 56
    rows, columns = matrix.shape
    submatrices = []
    for sub_rows in range(1, rows + 1):
        for sub_columns in range(1, columns + 1):
            for i in range(rows - sub_rows + 1):
                for j in range(columns - sub_columns + 1):
                    if is_valid_submatrix(i, j, sub_rows, sub_columns):
                        submatrix = matrix[i:i + sub_rows, j:j + sub_columns]
                        submatrices.append(submatrix.tolist())
    return submatrices