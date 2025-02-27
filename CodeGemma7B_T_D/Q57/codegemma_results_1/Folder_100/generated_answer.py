import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals 28.

    Args:
        matrix: A two-dimensional numpy matrix of integers.

    Returns:
        A list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 28. If no such submatrix is found, the function should return an empty list.
    """
    num_rows, num_cols = matrix.shape
    submatrices = []
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i, num_rows):
                for l in range(j, num_cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == 28:
                        submatrices.append(submatrix)
    return submatrices