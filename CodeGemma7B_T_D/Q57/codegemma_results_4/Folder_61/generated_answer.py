import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  Finds all submatrices of a given matrix with a sum of 8.

  Args:
    matrix: A two-dimensional numpy matrix of integers.

  Returns:
    A list of all submatrices with a sum of 8. If no submatrix is found, an empty list is returned.
  """
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.item(0) + submatrix.item(4) + submatrix.item(8) + submatrix.item(12) == 8:
                        submatrices.append(submatrix)
    return submatrices