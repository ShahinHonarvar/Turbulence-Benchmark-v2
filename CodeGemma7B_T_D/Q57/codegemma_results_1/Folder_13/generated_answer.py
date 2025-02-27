import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    The function returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 382.
    """
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for width in range(j + 1, len(matrix[0]) + 1):
                for height in range(i + 1, len(matrix) + 1):
                    submatrix = matrix[i:height, j:width]
                    if np.sum(submatrix) == 382:
                        result.append(submatrix)
    return result