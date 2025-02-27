import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  Returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 3.

  Args:
    matrix: A two-dimensional numpy matrix of integers.

  Returns:
    A list of submatrices, or an empty list if no submatrix with sum 3 exists.
  """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == 3:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices