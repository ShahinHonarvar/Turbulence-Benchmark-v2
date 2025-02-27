def submatrix_with_particular_sum(matrix):
    """
  Returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 94.

  Args:
    matrix: A two-dimensional numpy matrix of integers.

  Returns:
    The list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 94. If no such submatrix is found, the function should return an empty list.
  """
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 94:
                        result.append(submatrix)
    return result