import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mtx):
        rows, cols = mtx.shape
        submatrices = []
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row, rows):
                    for end_col in range(start_col, cols):
                        submatrices.append(mtx[start_row:end_row + 1, start_col:end_col + 1])
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submatrix.tolist() for submatrix in submatrices if np.sum(submatrix) == 88]
    return result