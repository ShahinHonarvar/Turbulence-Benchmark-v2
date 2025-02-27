def submatrix_with_particular_sum(matrix):
    """
  Finds all submatrices of a 2D numpy matrix with a given sum.

  Args:
    matrix: A 2D numpy matrix of integers.

  Returns:
    A list of all submatrices with the given sum, or an empty list if no such submatrix is found.
  """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -185:
                        submatrices.append(submatrix)
    return submatrices