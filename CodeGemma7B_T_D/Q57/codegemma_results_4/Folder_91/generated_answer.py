import numpy as np

def submatrix_with_particular_sum(matrix) -> list:
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -6. If no such submatrix is found, the function should return an empty list.
    """
    result = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix) + 1):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0]) + 1):
                    submatrix = matrix[i:j, k:l]
                    if submatrix.sum() == -6:
                        result.append(submatrix)
    return result