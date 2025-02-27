import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_193_submatrices(rows, cols):
        return sum(((rows - i) * (cols - j) == 193 for i in range(rows + 1) for j in range(cols + 1)))
    rows, cols = matrix.shape
    return count_193_submatrices(rows, cols)