def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices in the given matrix
    that contain 13 integers each.
    Args:
        matrix (numpy.ndarray): A 2D numpy matrix of integers.
    Returns:
        int: The number of submatrices that contain 13 integers.
    """
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix_count = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            submatrix_count += matrix[m][n]
                    if submatrix_count == 13:
                        count += 1
    return count