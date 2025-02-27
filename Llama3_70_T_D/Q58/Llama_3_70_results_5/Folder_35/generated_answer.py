import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for row in range(rows):
            for col in range(cols):
                for sub_row in range(row, rows):
                    for sub_col in range(col, cols):
                        submatrix = matrix[row:sub_row + 1, col:sub_col + 1]
                        if np.all(submatrix == 111) and submatrix.size == n:
                            count += 1
        return count
    n = 111
    return count_submatrices(matrix, n)