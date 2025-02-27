import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_127(matrix, n):
        submatrix = matrix[:n, :n]
        return submatrix.size - len(np.where(submatrix != 127)[0])
    rows, cols = matrix.shape
    return sum((count_127(matrix, n) for n in range(1, rows + cols - 1) if n <= rows - 1 or n <= cols - 1))