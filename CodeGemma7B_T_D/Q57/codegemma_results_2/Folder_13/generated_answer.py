import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices with a given sum.

    Args:
    matrix: The input matrix.

    Returns:
    A list of submatrices with the given sum, or an empty list if none is found.
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 382:
                        submatrices.append(submatrix)
    return submatrices