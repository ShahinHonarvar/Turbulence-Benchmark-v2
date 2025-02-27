import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes two-dimensional numpy matrix of integers as input and returns
    the list of all submatrices of the given matrix such that the sum
    of all integers in each submatrix equals 69.
    If no such submatrix is found, an empty list is returned.
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[k])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 69:
                        submatrices.append(submatrix)
    return submatrices