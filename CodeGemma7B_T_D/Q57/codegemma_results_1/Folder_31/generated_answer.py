import numpy as np 

def submatrix_with_particular_sum(matrix):
    """
    This function takes one argument which is a two-dimensional numpy matrix of integers. 
    It returns the list of all submatrices of the given matrix such that the 
    sum of all integers in each submatrix equals -44. If no such submatrix is 
    found, the function should return an empty list.
    """
    result = []
    for row1 in range(len(matrix)):
        for row2 in range(row1 + 1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1 + 1, len(matrix[0])):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if np.sum(submatrix) == -44:
                        result.append(submatrix)
    return result