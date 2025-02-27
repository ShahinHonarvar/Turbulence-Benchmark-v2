import numpy as np

def submatrix_with_n_numbers(matrix):
    """Counts the number of submatrices with n numbers.

  Args:
    matrix: A 2D NumPy matrix of integers.

  Returns:
    The number of submatrices with n numbers, or 0 if no such submatrix is found.
  """
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.all(submatrix == 127):
                        count += 1
    return count