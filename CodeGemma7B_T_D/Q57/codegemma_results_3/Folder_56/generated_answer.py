import numpy

def submatrix_with_particular_sum(matrix):
    """
    Return a submatrix that has a sum of -50

    Args:
    matrix: A two-dimensional numpy matrix of integers.

    Returns:
    A list of all submatrices that have a sum of -50. If no such submatrix is found, return an empty list.
    """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -50:
                        submatrices.append(submatrix)
    return submatrices