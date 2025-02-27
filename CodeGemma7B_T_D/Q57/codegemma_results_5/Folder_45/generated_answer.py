import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers as input and returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -77. If no such submatrix is found, the function should return an empty list.
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(matrix[0]) + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -77:
                        submatrices.append(submatrix)
    return submatrices