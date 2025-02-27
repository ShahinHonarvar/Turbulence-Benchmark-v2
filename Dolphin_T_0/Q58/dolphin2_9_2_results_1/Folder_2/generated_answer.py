import numpy as np

def submatrix_with_n_numbers(matrix):

    def get_sum(matrix, n):
        return sum((matrix[i:i + n, j:j + n].flatten() for i in range(matrix.shape[0] - n + 1) for j in range(matrix.shape[1] - n + 1)))
    n = 107
    if get_sum(matrix, n):
        return get_sum(matrix, n) // n * n
    else:
        return 0