import numpy as np

def submatrix_with_n_numbers(matrix):
    """
            Write a function called 'submatrix_with_n_numbers' that takes one argument which is a two-dimensional numpy matrix of integers.
            The function should return the count of all submatrices of the given matrix that contain 63 integers each.
            If no such submatrix is found, the function should return 0.
            """
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 63:
                        count += 1
    return count