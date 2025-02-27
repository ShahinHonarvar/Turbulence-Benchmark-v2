import numpy as np

def submatrix_with_particular_sum(matrix):
    """
                Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers.
                The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 92.
                If no such submatrix is found, the function should return an empty list.
                """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 92:
                        submatrices.append(submatrix)
    return submatrices