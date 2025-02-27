import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  Returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 42.

  Args:
    matrix: A 2-dimensional numpy matrix of integers.

  Returns:
    A list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -811. If no such submatrix is found, an empty list is returned.
  """
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if matrix[k][l] - matrix[i][j] == -811:
                        result.append(matrix[i:k + 1, j:l + 1])
    return result