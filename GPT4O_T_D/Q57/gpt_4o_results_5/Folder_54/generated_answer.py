import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(start_row, start_col, end_row, end_col):
        return np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1])
    rows, cols = matrix.shape
    result = []
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if get_submatrix_sum(r1, c1, r2, c2) == -59:
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1].tolist()
                        result.append(submatrix)
    return result