import numpy as np

def submatrix_with_n_numbers(matrix):
    return sum((1 for row in range(len(matrix)) if matrix[row].shape[0] == 10))