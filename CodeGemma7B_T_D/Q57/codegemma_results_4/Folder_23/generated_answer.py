import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 59. If no such submatrix is found, the function should return an empty list.
    """
    return [[i, j, k, l] for i in range(len(matrix)) for j in range(i, len(matrix)) for k in range(len(matrix[0])) for l in range(k, len(matrix[0])) if matrix[i:j + 1, k:l + 1].sum() == 59]