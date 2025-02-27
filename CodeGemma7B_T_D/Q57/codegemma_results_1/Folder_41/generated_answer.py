import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -26.

    Args:
    matrix: A two-dimensional numpy matrix of integers.

    Returns:
    A list of tuples, where each tuple represents a submatrix.
    """
    submatrices = []
    for row1 in range(len(matrix)):
        for row2 in range(row1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1, len(matrix[0])):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if np.sum(submatrix) == -26:
                        submatrices.append(tuple(submatrix.flatten()))
    return submatrices