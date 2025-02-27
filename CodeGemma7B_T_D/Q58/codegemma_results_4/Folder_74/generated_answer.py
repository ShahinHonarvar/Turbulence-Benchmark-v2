from itertools import product

def submatrix_with_n_numbers(matrix):
    """
  Write a function called 'submatrix_with_n_numbers' that takes one argument which is a two-dimensional numpy matrix of integers.
  The function should return the count of all submatrices of the given matrix that contain 48 integers each.
  If no such submatrix is found, the function should return 0.
  """
    rows, cols = matrix.shape
    count = 0
    for i, j in product(range(rows), range(cols)):
        for k, l in product(range(i, rows), range(j, cols)):
            submatrix = matrix[i:k + 1, j:l + 1]
            if np.all(submatrix == 48):
                count += 1
    return count