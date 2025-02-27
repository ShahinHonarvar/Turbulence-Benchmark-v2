import numpy as np

def submatrix_with_n_numbers(matrix):
    """
  Counts the number of submatrices of a given matrix with n integers each.

  Args:
    matrix: A two-dimensional numpy matrix of integers.

  Returns:
    The count of all submatrices of the given matrix that contain n integers each.
  """
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 33:
                        count += 1
    return count