import numpy as np

def submatrix_with_n_numbers(matrix):
    """
            Write a function called 'submatrix_with_n_numbers' that takes one argument which is a two-dimensional numpy matrix of integers.
            The function should return the count of all submatrices of the given matrix that contain 42 integers each. If no such submatrix is found, the function should return 0.
            """
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for width in range(1, len(matrix) + 1 - j):
                for height in range(1, len(matrix[0]) + 1 - i):
                    submatrix = matrix[j:j + width, i:i + height]
                    if np.count_nonzero(submatrix == 42) == 42:
                        count += 1
    return count