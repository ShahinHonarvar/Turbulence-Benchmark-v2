import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Write a function called 'submatrix_with_n_numbers' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the count of all submatrices of the given matrix that contain 45 integers each. If no such submatrix is found, the function should return 0.

    """
    count = 0
    dim0, dim1 = matrix.shape
    for i0 in range(dim0):
        for j0 in range(dim1):
            for i1 in range(i0, dim0):
                for j1 in range(j0, dim1):
                    submatrix = matrix[i0:i1 + 1, j0:j1 + 1]
                    if submatrix.shape[0] * submatrix.shape[1] == 45:
                        count += 1
    return count