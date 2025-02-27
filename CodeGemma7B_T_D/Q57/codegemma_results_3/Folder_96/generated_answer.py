from itertools import combinations_with_replacement

def submatrix_with_particular_sum(matrix):
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers.
    The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -63.
    If no such submatrix is found, the function should return an empty list.
    """
    result = []
    for r1, r2 in combinations_with_replacement(range(len(matrix)), 2):
        for c1, c2 in combinations_with_replacement(range(len(matrix[0])), 2):
            submatrix = matrix[r1:r2 + 1][:, c1:c2 + 1]
            if submatrix.sum() == -63:
                result.append(submatrix)
    return result