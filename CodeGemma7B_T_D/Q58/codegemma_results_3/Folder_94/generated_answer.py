import numpy as np

def submatrix_with_n_numbers(matrix):
    """
  Counts the number of submatrices with 93 integers each in a given numpy matrix.
  
  Args:
    matrix: A two-dimensional numpy matrix of integers.
  
  Returns:
    The count of all submatrices of the given matrix that contain 93 integers each. If no such submatrix is found, the function should return 0.
  """
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 93:
                        count += 1
    return count