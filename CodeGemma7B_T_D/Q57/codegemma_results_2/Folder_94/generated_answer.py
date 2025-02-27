import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes one argument which is a two-dimensional numpy matrix of integers.
    The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 92.
    If no such submatrix is found, the function should return an empty list.
    """
    output = []
    values = matrix.cumsum(axis=0).cumsum(axis=1)
    for r1 in range(matrix.shape[0] + 1):
        for r2 in range(r1, matrix.shape[0] + 1):
            for c1 in range(matrix.shape[1] + 1):
                for c2 in range(c1, matrix.shape[1] + 1):
                    matrix_sum = values[r2, c2] - (values[r1, c2] + values[r2, c1] - values[r1, c1])
                    if matrix_sum == 92:
                        output.append([row[c1:c2] for row in matrix[r1:r2]])
    return output