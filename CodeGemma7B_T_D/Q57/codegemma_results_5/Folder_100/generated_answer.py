import numpy as np

def submatrix_with_particular_sum(matrix):
    """Given a numpy matrix of integers, returns the list of all submatrices that have the sum of all integers equal to 28.
            """
    result = []
    for i in range(matrix.shape[0]):
        for j in range(i + 1, matrix.shape[0]):
            for k in range(matrix.shape[1]):
                for l in range(k + 1, matrix.shape[1]):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if submatrix.sum() == 28:
                        result.append(submatrix)
    return result