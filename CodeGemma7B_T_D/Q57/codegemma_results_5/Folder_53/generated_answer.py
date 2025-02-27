def submatrix_with_particular_sum(matrix):
    """
    :type matrix: numpy.ndarray
    """
    col_cumsums = np.zeros_like(matrix, dtype=int)
    col_cumsums[:, 0] = matrix[:, 0]
    for col in range(1, matrix.shape[1]):
        col_cumsums[:, col] = col_cumsums[:, col - 1] + matrix[:, col]
    for row_start in range(matrix.shape[0]):
        for row_end in range(row_start, matrix.shape[0]):
            row_range = slice(row_start, row_end + 1)
            for col_start in range(matrix.shape[1]):
                for col_end in range(col_start, matrix.shape[1]):
                    col_range = slice(col_start, col_end + 1)
                    submatrix_sum = col_cumsums[row_range, col_end] - col_cumsums[row_range, col_start - 1 if col_start > 0 else 0]
                    if submatrix_sum == -37:
                        return [matrix[row_range, col_range]]
    return []