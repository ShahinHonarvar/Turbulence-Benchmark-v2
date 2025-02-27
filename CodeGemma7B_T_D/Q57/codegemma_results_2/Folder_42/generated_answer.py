import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 862.

    Args:
        matrix: A two-dimensional numpy matrix of integers.

    Returns:
        A list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 862. If no such submatrix is found, the function should return an empty list.
    """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == 862:
                        submatrices.append(submatrix)
    return submatrices