import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers as input and returns the list
    of all submatrices of the given matrix such that the sum of all integers in each submatrix
    equals 84. If no such submatrix is found, the function returns an empty list.
    """
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 84:
                        result.append(submatrix)
    return result