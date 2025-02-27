import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers and returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 95.
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 95:
                        submatrices.append(submatrix)
    return submatrices