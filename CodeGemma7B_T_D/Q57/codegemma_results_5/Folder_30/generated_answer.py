import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers.
    The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 21. If no such submatrix is found, the function should return an empty list.
    """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrix = matrix[i, j]
            submatrix_sum = matrix[i, j]
            if submatrix_sum == 21:
                submatrices.append(submatrix)
    return submatrices