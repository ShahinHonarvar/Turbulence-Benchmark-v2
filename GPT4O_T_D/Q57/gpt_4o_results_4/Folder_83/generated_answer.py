import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices_of_size(r1, c1, r2, c2):
        return matrix[r1:r2, c1:c2]
    rows, cols = matrix.shape
    solution_submatrices = []
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows + 1):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols + 1):
                    submatrix = get_submatrices_of_size(r1, c1, r2, c2)
                    if np.sum(submatrix) == -15:
                        solution_submatrices.append(submatrix)
    return solution_submatrices