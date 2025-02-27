import numpy as np

def submatrix_with_n_numbers(matrix):
    """
            This function takes one argument which is a two-dimensional numpy matrix of integers.
            The function returns the count of all submatrices of the given matrix that contain 17 integers each.
            If no such submatrix is found, the function returns 0.
            """
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1):
                for l in range(j + 1):
                    submatrix = matrix[k:i + 1, l:j + 1]
                    if len(submatrix) == 17:
                        count += 1
    return count