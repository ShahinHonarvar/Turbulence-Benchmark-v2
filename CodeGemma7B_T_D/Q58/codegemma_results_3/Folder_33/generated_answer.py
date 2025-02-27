def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices of the given matrix that contain 118 integers each.

    Args:
        matrix: A two-dimensional numpy matrix of integers.

    Returns:
        The count of submatrices with 118 integers each.
    """
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    if matrix[k][l] - matrix[k][j] - matrix[i][l] + matrix[i][j] == 118:
                        count += 1
    return count