def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices of a given matrix that contain 131 integers each.

    Args:
    matrix: A two-dimensional numpy matrix of integers.

    Returns:
    The count of submatrices with 131 integers each.
    """
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    if (matrix[i:k + 1, j:l + 1] == 131).all():
                        count += 1
    return count