import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes one argument which is a two-dimensional numpy matrix of integers.
    The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -65.
    If no such submatrix is found, the function should return an empty list.
    """

    def is_submatrix_with_sum(matrix, i, j, k, l):
        """
        This function checks if the submatrix of the given matrix with the top-left corner at (i, j) and the bottom-right corner at (k, l) has a sum of -65.
        """
        sum = 0
        for row in range(i, k + 1):
            for col in range(j, l + 1):
                sum += matrix[row][col]
        return sum == -65
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if is_submatrix_with_sum(matrix, i, j, k, l):
                        submatrices.append((i, j, k, l))
    return submatrices