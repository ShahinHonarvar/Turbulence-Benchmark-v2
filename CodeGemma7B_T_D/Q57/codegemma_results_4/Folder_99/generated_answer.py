import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  This function returns the list of all submatrices of the given matrix with a sum of -185.

  Args:
    matrix: A numpy array representing the matrix.

  Returns:
    A list of all submatrices with a sum of -185, or an empty list if there are none.
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