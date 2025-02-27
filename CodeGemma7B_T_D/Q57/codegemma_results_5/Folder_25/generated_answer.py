import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    """This function takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -20. If no such submatrix is found, the function should return an empty list."""
    result = []
    for r1, r2 in product(range(len(matrix)), range(len(matrix))):
        for c1, c2 in product(range(len(matrix[0])), range(len(matrix[0]))):
            submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
            if np.sum(submatrix) == -20:
                result.append(submatrix)
    if not result:
        return []
    return result