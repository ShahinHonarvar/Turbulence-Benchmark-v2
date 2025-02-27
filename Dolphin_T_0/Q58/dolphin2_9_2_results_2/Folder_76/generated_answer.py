import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a 2D numpy matrix of integers as an argument
    and returns the count of all submatrices containing 159 integers each.
    If no such submatrix is found, it returns 0.
    """
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i:i + 13, j:j + 13].sum() == 159:
                count += 1
    return count