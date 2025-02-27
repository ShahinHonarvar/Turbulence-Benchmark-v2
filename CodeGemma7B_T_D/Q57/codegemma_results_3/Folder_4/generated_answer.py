import numpy as np

def submatrix_with_particular_sum(matrix):
    """
            This function returns a list of all submatrices of the given matrix
            such that the sum of all integers in each submatrix equals 87.

            Args:
                matrix: A two-dimensional numpy matrix of integers.

            Returns:
                A list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 87. If no such submatrix is found, the function should return an empty list.
            """
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.sum() == 87:
                        submatrices.append(submatrix)
    return submatrices