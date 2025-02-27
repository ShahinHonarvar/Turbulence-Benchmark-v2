import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers and returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 95.

    Args:
        matrix: A two-dimensional numpy matrix of integers.

    Returns:
        A list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 95. If no such submatrix is found, the function should return an empty list.
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k, len(matrix[0])):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if np.sum(submatrix) == 95:
                        submatrices.append(submatrix)
    return submatrices