import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(matrix, top_left, bottom_right):
        r1, c1 = top_left
        r2, c2 = bottom_right
        sub = matrix[r1:r2 + 1, c1:c2 + 1]
        return np.sum(sub)
    rows, cols = matrix.shape
    submatrices = []
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if submatrix_sum(matrix, (r1, c1), (r2, c2)) == 69:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1].tolist())
    return submatrices