import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of a given matrix with a sum of 84.

    Args:
      matrix: A two-dimensional numpy matrix of integers.

    Returns:
      A list of all submatrices of the given matrix with a sum of 84.
    """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 84:
                        submatrices.append(submatrix)
    return submatrices