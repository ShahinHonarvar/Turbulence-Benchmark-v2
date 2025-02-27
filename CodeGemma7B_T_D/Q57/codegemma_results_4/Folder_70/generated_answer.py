import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function finds all submatrices of a given matrix with a sum of 411.

    Args:
        matrix: A two-dimensional numpy matrix of integers.

    Returns:
        A list of all submatrices with a sum of 411. If no such submatrix is found, an empty list is returned.
    """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 411:
                        submatrices.append(submatrix)
    return submatrices