def submatrix_with_n_numbers(matrix):
    """
  Counts the number of submatrices of the given matrix that contain 54 integers each.

  Args:
    matrix: A two-dimensional numpy matrix of integers.

  Returns:
    The count of submatrices that contain 54 integers each.
  """
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if len(set(matrix[i:k + 1, j:l + 1].flatten())) == 54:
                        count += 1
    return count