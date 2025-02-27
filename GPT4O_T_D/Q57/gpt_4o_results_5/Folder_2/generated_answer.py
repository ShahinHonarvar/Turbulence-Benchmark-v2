import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(matrix, top_left, bottom_right):
        r1, c1 = top_left
        r2, c2 = bottom_right
        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
        return (submatrix.sum(), submatrix.tolist())

    def all_submatrices(matrix):
        rows, cols = matrix.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        yield ((r1, c1), (r2, c2))
    result = []
    for top_left, bottom_right in all_submatrices(matrix):
        sub_sum, sub = submatrix_sum(matrix, top_left, bottom_right)
        if sub_sum == -863:
            result.append(sub)
    return result