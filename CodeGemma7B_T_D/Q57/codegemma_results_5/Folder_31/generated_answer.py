def submatrix_with_particular_sum(matrix):
    """Submatrix with particular sum.

    :type matrix: numpy.ndarray
    :rtype: list
    """
    submatrices = []
    for row_start in range(len(matrix)):
        for row_end in range(row_start, len(matrix)):
            for col_start in range(len(matrix[0])):
                for col_end in range(col_start, len(matrix[0])):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if submatrix.sum() == -44:
                        submatrices.append(submatrix)
    return submatrices