import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -3. If no such submatrix is found, the function should return an empty list.
  """
    submatrices = []
    for top_row in range(len(matrix)):
        for left_col in range(len(matrix[0])):
            for bottom_row in range(top_row, len(matrix)):
                for right_col in range(left_col, len(matrix[0])):
                    submatrix = matrix[top_row:bottom_row + 1, left_col:right_col + 1]
                    if np.sum(submatrix) == -3:
                        submatrices.append(submatrix)
    return submatrices