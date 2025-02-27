import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(matrix):
        n, m = matrix.shape
        for row_start in range(n):
            for row_end in range(row_start, n):
                for col_start in range(m):
                    for col_end in range(col_start, m):
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        yield submatrix
    result = []
    for submatrix in generate_submatrices(matrix):
        if np.sum(submatrix) == -57:
            result.append(submatrix.tolist())
    return result