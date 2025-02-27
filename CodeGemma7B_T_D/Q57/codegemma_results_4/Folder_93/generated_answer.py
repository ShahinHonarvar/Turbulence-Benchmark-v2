import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers.
    The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -65.
    If no such submatrix is found, the function should return an empty list.
    """
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for width in range(1, len(matrix) - i + 1):
                for height in range(1, len(matrix[0]) - j + 1):
                    submatrix = matrix[i:i + width, j:j + height]
                    if np.sum(submatrix) == -65:
                        result.append(submatrix)
    return result