import numpy as np

def submatrix_with_n_numbers(matrix):
    """
  Counts the number of submatrices with n numbers in a given matrix.

  Args:
    matrix: A 2D numpy matrix of integers.

  Returns:
    The count of submatrices with n numbers.
  """
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 131:
                        count += 1
    return count