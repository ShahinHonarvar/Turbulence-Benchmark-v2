import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        for rb in range(rows):
            for re in range(rb + 1, rows + 1):
                for cb in range(cols):
                    for ce in range(cb + 1, cols + 1):
                        yield matrix[rb:re, cb:ce]
    result = []
    for submatrix in get_submatrices(matrix):
        if np.sum(submatrix) == 88:
            result.append(submatrix.tolist())
    return result