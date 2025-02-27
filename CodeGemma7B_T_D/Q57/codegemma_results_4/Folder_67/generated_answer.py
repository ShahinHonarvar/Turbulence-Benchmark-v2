import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers and returns the list of all submatrices with a sum of 40.
    """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            sum += matrix[m][n]
                    if sum == 40:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices