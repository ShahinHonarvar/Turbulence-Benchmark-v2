import numpy as np

def submatrix_with_n_numbers(matrix):
    """Counts the number of submatrices of a given matrix containing n numbers.

    Args:
      matrix: A two-dimensional numpy matrix of integers.

    Returns:
      The count of all submatrices of the given matrix that contain 159 integers each.
    """
    x, y = matrix.shape
    count = 0
    for i in range(x):
        for j in range(y):
            for k in range(i, x):
                for l in range(j, y):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 159:
                        count += 1
    return count