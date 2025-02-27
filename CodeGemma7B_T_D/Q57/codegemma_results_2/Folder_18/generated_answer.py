def submatrix_with_particular_sum(matrix):
    """
  This function takes one argument which is a two-dimensional numpy matrix of integers and
  returns the list of all submatrices of the given matrix such that the sum of all
  integers in each submatrix equals 616. If no such submatrix is found, the function
  should return an empty list.
  """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j - 1, len(matrix[k])):
                    if sum((matrix[m][n] for m in range(i, k + 1) for n in range(j, l + 1))) == 616:
                        return [[matrix[m][n] for n in range(j, l + 1)] for m in range(i, k + 1)]
    return []