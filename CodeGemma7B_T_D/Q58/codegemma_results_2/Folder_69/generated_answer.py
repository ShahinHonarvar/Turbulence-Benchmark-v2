import numpy as np

def submatrix_with_n_numbers(matrix):
    """
  Write a function called 'submatrix_with_n_numbers' that takes one argument which is a two-dimensional numpy matrix of integers.
  The function should return the count of all submatrices of the given matrix that contain 126 integers each.
  If no such submatrix is found, the function should return 0.
  """
    count = 0
    for size in range(1, len(matrix) + 1):
        for i in range(len(matrix) - size + 1):
            for j in range(len(matrix[0]) - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.all(submatrix == 126):
                    count += 1
    return count