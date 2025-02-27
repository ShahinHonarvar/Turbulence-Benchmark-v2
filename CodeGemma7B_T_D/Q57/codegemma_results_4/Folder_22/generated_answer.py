def submatrix_with_particular_sum(matrix):
    """
  Finds all submatrices of a given matrix with a specific sum.

  Args:
    matrix: A two-dimensional numpy matrix of integers.

  Returns:
    A list of all submatrices with a sum of -38, or an empty list if no such submatrix is found.
  """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix) + 1):
            for k in range(len(matrix)):
                for l in range(k + 1, len(matrix) + 1):
                    submatrix = matrix[i:j, k:l]
                    submatrices.append(submatrix)
    submatrices_with_sum = []
    for submatrix in submatrices:
        if submatrix.sum() == -38:
            submatrices_with_sum.append(submatrix)
    return submatrices_with_sum