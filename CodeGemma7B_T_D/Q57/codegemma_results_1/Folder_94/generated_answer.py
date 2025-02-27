import numpy as np

def submatrix_with_particular_sum(matrix):
    """
            This function takes a 2-dimensional numpy matrix as an argument and returns a list of all submatrices with a sum of 92.
            """
    n = matrix.shape[0]
    submatrices = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(n):
                for l in range(k + 1, n + 1):
                    submatrix = matrix[i:j, k:l]
                    if submatrix.sum() == 92:
                        submatrices.append(submatrix)
    return submatrices