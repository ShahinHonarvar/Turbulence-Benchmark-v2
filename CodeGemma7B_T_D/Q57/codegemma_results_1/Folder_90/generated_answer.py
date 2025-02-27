import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  This function finds all submatrices in a given matrix with a particular sum.

  Args:
    matrix: A two-dimensional numpy matrix of integers.

  Returns:
    A list of all submatrices in the given matrix with a particular sum. If no such submatrix is found, the function should return an empty list.
  """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    sum = 0
                    for m in range(k, l + 1):
                        for n in range(j, l + 1):
                            sum += matrix[m][n]
                    if sum == -452:
                        submatrices.append((i, j, k, l))
    return submatrices