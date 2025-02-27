import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers and returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 3.
    """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 3:
                        submatrices.append(submatrix)
    return submatrices