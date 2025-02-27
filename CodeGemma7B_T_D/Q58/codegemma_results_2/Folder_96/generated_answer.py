def submatrix_with_n_numbers(matrix):
    """
    This function counts the number of submatrices with n numbers in a 2D numpy matrix.

    Args:
    matrix: A 2D numpy matrix of integers.

    Returns:
    The number of submatrices with n numbers.
    """
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 20:
                        submatrix_count += 1
    return submatrix_count