import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_sum_of_submatrix(matrix, r1, c1, r2, c2):
        return np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
    submatrices = []
    num_rows, num_cols = matrix.shape
    for r1 in range(num_rows):
        for r2 in range(r1, num_rows):
            for c1 in range(num_cols):
                for c2 in range(c1, num_cols):
                    if get_sum_of_submatrix(matrix, r1, c1, r2, c2) == 21:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1].tolist())
    return submatrices