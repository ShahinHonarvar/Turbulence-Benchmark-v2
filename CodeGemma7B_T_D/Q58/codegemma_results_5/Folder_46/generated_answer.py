def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices of a given matrix that contain a specific number of integers.

    Args:
        matrix: A two-dimensional numpy matrix of integers.

    Returns:
        The number of submatrices that contain the specified number of integers.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i, num_rows):
                for l in range(j, num_cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 144:
                        count += 1
    return count