import numpy as np

def submatrix_with_particular_sum(matrix):

    def compute_submatrix_sum(matrix, top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        submatrices = []
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top, rows):
                    for right in range(left, cols):
                        yield matrix[top:bottom + 1, left:right + 1]
    submatrices = list(get_submatrices(matrix))
    result = []
    for submatrix in submatrices:
        if compute_submatrix_sum(submatrix, 0, 0, submatrix.shape[0] - 1, submatrix.shape[1] - 1) == -255:
            result.append(submatrix)
    return result