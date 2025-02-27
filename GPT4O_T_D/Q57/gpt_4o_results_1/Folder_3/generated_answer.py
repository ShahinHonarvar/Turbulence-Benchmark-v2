import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for r1 in range(rows):
            for r2 in range(r1 + 1, rows + 1):
                for c1 in range(cols):
                    for c2 in range(c1 + 1, cols + 1):
                        submatrix = matrix[r1:r2, c1:c2]
                        submatrices.append(submatrix)
        return submatrices
    valid_submatrices = []
    submatrices = find_submatrices(matrix)
    for submatrix in submatrices:
        if np.sum(submatrix) == 54:
            valid_submatrices.append(submatrix)
    return valid_submatrices