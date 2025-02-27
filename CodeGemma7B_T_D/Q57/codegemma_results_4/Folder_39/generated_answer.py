import numpy as np

def submatrix_with_particular_sum(matrix):
    """
            Returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 66.

            Args:
                matrix: A two-dimensional numpy matrix of integers.

            Returns:
                A list of submatrices of the given matrix such that the sum of all integers in each submatrix equals 66. If no such submatrix is found, the function should return an empty list.
            """
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(i, rows):
            for k in range(cols):
                for l in range(k, cols):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    sum = np.sum(submatrix)
                    if sum == 66:
                        submatrices.append(submatrix)
    return submatrices