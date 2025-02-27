import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes one argument which is a two-dimensional numpy matrix of integers. 
    It returns the count of all submatrices of the given matrix that contain 191 integers each.
    If no such submatrix is found, the function returns 0.
    """
    m, n = matrix.shape
    count = 0
    for i in range(m - 190):
        for j in range(n - 190):
            if matrix[i:i + 191, j:j + 191].sum() == 191 * 191:
                count += 1
    return count