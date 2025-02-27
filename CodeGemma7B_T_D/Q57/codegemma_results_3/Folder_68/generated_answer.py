import numpy as np

def submatrix_with_particular_sum(matrix):
    """
            This function takes one argument which is a two-dimensional numpy matrix of integers.
            The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 3.
            If no such submatrix is found, the function should return an empty list.
            """
    if not matrix.size:
        return []
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 3:
                        submatrices.append(submatrix)
    return submatrices