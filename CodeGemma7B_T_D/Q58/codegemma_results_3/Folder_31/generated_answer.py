def submatrix_with_n_numbers(matrix):
    """
  Write a function called 'submatrix_with_n_numbers' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the count of all submatrices of the given matrix that contain 45 integers each. If no such submatrix is found, the function should return 0.
  """
    num_rows, num_cols = matrix.shape
    count = 0
    for row1 in range(num_rows):
        for row2 in range(row1, num_rows):
            for col1 in range(num_cols):
                for col2 in range(col1, num_cols):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if submatrix.size == 45:
                        count += 1
    return count