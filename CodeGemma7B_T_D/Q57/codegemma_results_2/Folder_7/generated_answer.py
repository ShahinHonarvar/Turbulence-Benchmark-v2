import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  Finds submatrices with a specific sum.

  Args:
    matrix: A 2D NumPy matrix of integers.

  Returns:
    A list of submatrices with the given sum, or an empty list if none are found.
  """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -128:
                        submatrices.append(submatrix)
    return submatrices