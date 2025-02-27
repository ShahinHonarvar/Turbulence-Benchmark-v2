import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix, top, left, bottom, right):
        return [matrix[i][left:right + 1] for i in range(top, bottom + 1)]

    def submatrix_sum(submatrix):
        return sum((sum(row) for row in submatrix))
    submatrices = []
    rows, cols = matrix.shape
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submatrix = get_submatrices(matrix, top, left, bottom, right)
                    if submatrix_sum(submatrix) == 8:
                        submatrices.append(submatrix)
    return submatrices