import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  This function finds all submatrices of a given matrix with a sum of -50.

  Args:
    matrix: A two-dimensional NumPy matrix of integers.

  Returns:
    A list of all submatrices with a sum of -50. If no such submatrix is found, an empty list is returned.
  """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            columns = []
            for k in range(len(matrix[0])):
                sum_of_column = matrix[i][k] + matrix[j][k]
                columns.append(k)
            if sum_of_column == -50:
                submatrices.append(matrix[i:j + 1, columns])
    return submatrices