import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes one argument which is a two-dimensional numpy matrix of
    integers. The function should return the list of all submatrices of the given
    matrix such that the sum of all integers in each submatrix equals -46.
    If no such submatrix is found, the function should return an empty list.
    """
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -46:
                        result.append(submatrix)
    return result