import numpy as np

def submatrix_with_n_numbers(matrix):
    """Counts the number of submatrices in a given matrix with n numbers each.

  Args:
    matrix: A two-dimensional numpy matrix of integers.

  Returns:
    The count of submatrices with n numbers each, or 0 if no such submatrix is found.
  """
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    if np.all(matrix[i:k + 1, j:l + 1] == 97):
                        count += 1
    return count