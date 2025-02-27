import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(matrix):
        return np.prod(matrix.shape)
    count = 0
    rows, cols = matrix.shape
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if count_elements(submatrix) == 93:
                        count += 1
    return count