import numpy as np

def submatrix_with_particular_sum(matrix):
    """
            This function takes one argument which is a two-dimensional numpy matrix of integers.
            The function should return the list of all submatrices of the given matrix
            such that the sum of all integers in each submatrix equals 35.
            If no such submatrix is found, the function should return an empty list.
            """
    array = matrix.flatten()
    submatrices = []
    for i in range(len(array)):
        for j in range(i + 1, len(array) + 1):
            submatrix = array[i:j]
            if submatrix.sum() == 35:
                submatrices.append(array[i:j])
    return submatrices