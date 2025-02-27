import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submatrix):
        return np.sum(submatrix)

    def generate_submatrices(matrix):
        rows, cols = matrix.shape
        for r1 in range(rows):
            for r2 in range(r1 + 1, rows + 1):
                for c1 in range(cols):
                    for c2 in range(c1 + 1, cols + 1):
                        yield matrix[r1:r2, c1:c2]
    target_sum = 35
    result = []
    for submatrix in generate_submatrices(matrix):
        if submatrix_sum(submatrix) == target_sum:
            result.append(submatrix)
    return result