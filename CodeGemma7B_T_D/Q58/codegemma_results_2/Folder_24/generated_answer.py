import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices of a given matrix that contain 51 integers each.

    Args:
        matrix: A two-dimensional numpy matrix of integers.

    Returns:
        The count of all submatrices of the given matrix that contain 51 integers each. If no such submatrix exists, the function should return 0.
    """
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    num_integers = submatrix.size
                    if num_integers == 51:
                        count += 1
    return count