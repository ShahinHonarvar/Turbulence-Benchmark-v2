import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  Function that takes one argument which is a two-dimensional numpy matrix of integers.
  The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -13.
  If no such submatrix is found, the function should return an empty list.
  """
    result = []
    for start_row in range(len(matrix)):
        for start_col in range(len(matrix[0])):
            for end_row in range(start_row, len(matrix)):
                for end_col in range(start_col, len(matrix[0])):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if np.sum(submatrix) == -13:
                        result.append(submatrix)
    return result